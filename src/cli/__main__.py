import os
import sys
import time
import argparse
import csv
import xlsxwriter

from textwrap import shorten
from tabulate import tabulate

from bf.__init__ import __module__, __project_name__, __project_description__, __project_version__
from bf.placesapi import PlacesAPI
from bf.latlng import LatLng

def save_csv(places, filename):
    """
    Guarda los lugares en un fichero CSV.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Escribir encabezados
        writer.writerow(["Nombre", "Tipo", "Dirección", "Teléfono", "Web", "Mapa", "Horario"])

        # Escribir datos de los objetos
        for place in places:
            writer.writerow([
                place.name, 
                place.type, 
                place.address, 
                place.phone, 
                place.website,
                place.mapLink,
                ",".join(place.timetable) if place.timetable else ""
            ])

def save_excel(places, filename, category):
    """
    Guarda los lugares en un fichero Excel.
    """    

    # Crear un fichero Excel
    workbook = xlsxwriter.Workbook(filename)

    # Crear una hoja de cálculo
    worksheet = workbook.add_worksheet(name=category)

    # Crear un formato en negrita
    bold_format = workbook.add_format({"bold": True})

    # Escribir encabezados
    fields = ["Nombre", "Tipo", "Dirección", "Teléfono", "Web", "Mapa", "Horario"]
    for col, value in enumerate(fields):
        worksheet.write(0, col, value, bold_format)

    # Escribir datos de los objetos
    col_widths = [0] * len(fields)
    row = 1
    for place in places:
        data = [
            place.name, 
            place.type, 
            place.address, 
            place.phone, 
            place.website,
            place.mapLink,
            ",".join(place.timetable) if place.timetable else ""
        ]
        col_widths = [max(col_widths[i], len(str(data[i]))) for i in range(len(fields))]
        for col, value in enumerate(data):
            worksheet.write(row, col, value)
        row += 1

    # Ajustar el ancho de las columnas
    for col, width in enumerate(col_widths):
        worksheet.set_column(col, col, width + 1)

    # Cerrar el fichero
    workbook.close()

def main():

    # declara un HelpFormatter personalizado para reemplazar el texto 'usage:' por 'Uso:'
    class CustomHelpFormatter(argparse.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix='Uso: '):
            if usage is not argparse.SUPPRESS:
                args = usage, actions, groups, prefix
                self._add_item(self._format_usage, args)

    # define el parser
    parser = argparse.ArgumentParser(prog=__module__, description=f"{__project_description__} (v{__project_version__})", epilog='¡Corre, que te las quita el César!', add_help=False, formatter_class=CustomHelpFormatter)

    # define los comandos (mutuamente excluyentes)
    commands = parser.add_argument_group('Comandos')
    commands = commands.add_mutually_exclusive_group(required=True)
    commands.add_argument('-h', '--help', action='store_true', help='Muestra esta ayuda y termina')
    commands.add_argument('-v', '--version', action='version', help='Mostrar versión', version=f'{__project_name__} v{__project_version__}')
    commands.add_argument('--search', action='store_true', help='Buscar empresas')

    # define las opciones adicionales a los comandos
    options = parser.add_argument_group('Opciones')
    options.add_argument('--category', metavar='CATEGORY', help='Categoría de las empresas a buscar', type=str)
    options.add_argument('--location', metavar='LOCATION', help='Ubicación para la búsqueda de empresas (p.ej. "Santa Cruz de Tenerife, España")', type=str)
    options.add_argument('--latlng', metavar='LATLNG', help='Ubicación para la búsqueda de empresas en formato "latitud,longitud"', type=str)
    options.add_argument('--radius', metavar='RADIUS', help='Radio en kilómetros para la búsqueda', default=5.0, type=float)
    options.add_argument('--csv', metavar='OUTPUT', nargs='?', const="output.csv", help='Fichero de salida en formato CSV', type=str)
    options.add_argument('--excel', metavar='OUTPUT', nargs='?', const="output.xlsx", help='Fichero de salida en formato XLSX', type=str)
    options.add_argument('--apikey', metavar='KEY', help='Clave de API de Google Places (si no se especifica, se buscará en las variables de entorno)', type=str)

    # parsea los argumentos
    args = parser.parse_args()

    # lógica según las opciones
    if args.help:
        parser.print_help()
        return

    start_time = time.time()

    if args.search:

        # Obtiene la clave de la API de Google Places
        if args.apikey:
            apikey = args.apikey
        else:
            apikey = os.getenv("GOOGLE_PLACES_API_KEY")
        
        if apikey is None:
            print("No se encontró la clave de la API de Google Places", file=sys.stderr)
            return

        # Realiza la búsqueda de empresas
        try:

            # Crea una instancia de la API de Google Places
            api = PlacesAPI(apikey)

            # Ubicación geográfica
            if args.latlng:
                latitude, longitude = map(float, args.latlng.split(","))
                latLng = LatLng(latitude, longitude)
            elif args.location:
                latLng = api.locate(args.location)

            location = args.location if args.location else args.latlng
            print(f"Buscando empresas de la categoría '{args.category}' en '{location}' con un radio de {args.radius} km...")

            # Realiza la búsqueda de empresas                
            places = api.search(args.category, latLng, args.radius)

            # Ordena los resultados por nombre
            places.sort(key=lambda place: place.name.lower())
            
        except Exception as e:
            print("Error en la búsqueda:", e.args[0], file=sys.stderr)
            return

        if args.csv:
            # Guardar los resultados en un fichero CSV
            save_csv(places, args.csv)
            # Mostrar mensaje de confirmación
            print(f"Resultados guardados en '{args.csv}'")

        if args.excel:
            # Guardar los resultados en un fichero XLSX
            save_excel(places, args.excel, args.category)
            # Mostrar mensaje de confirmación
            print(f"Resultados guardados en '{args.excel}'")
        
        if not args.csv and not args.excel:
            # Convertir objetos en una lista de listas
            places_data = [
                [
                    shorten(place.name, width=40, placeholder="..."), 
                    place.type, 
                    shorten(place.address, width=40, placeholder="..."), 
                    place.phone, 
                    place.website,
                ] for place in places
            ]
            # Mostrar la tabla con encabezados
            print(tabulate(places_data, headers=["Nombre", "Tipo", "Dirección", "Teléfono", "Web"], tablefmt="grid"))

        # Cantidad de empresas encontradas
        print(f"Se encontraron {len(places)} empresas")

    print(f"Tiempo transcurrido: {time.time() - start_time:.2f} s")

if __name__ == "__main__":
    main()

