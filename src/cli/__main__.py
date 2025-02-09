import os
import time
import argparse
import csv

from textwrap import shorten
from tabulate import tabulate

from bf.__init__ import __module__, __project_description__, __project_version__
from bf.placesapi import PlacesAPI

def save_csv(places, filename):
    """
    Guarda los lugares en un fichero CSV.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Escribir encabezados
        writer.writerow(["Nombre", "Tipo", "Dirección", "Estado", "Teléfono", "Web"])

        # Escribir datos de los objetos
        for place in places:
            writer.writerow([place.name, place.type, place.address, place.status, place.phone, place.website])

def main():

    # declara un HelpFormatter personalizado para reemplazar el texto 'usage:' por 'Uso:'
    class CustomHelpFormatter(argparse.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix='Uso: '):
            if usage is not argparse.SUPPRESS:
                args = usage, actions, groups, prefix
                self._add_item(self._format_usage, args)

    # define el parser
    parser = argparse.ArgumentParser(prog=__module__, description=__project_description__, epilog='¡Ahora ponte a buscar empresas!', add_help=False, formatter_class=CustomHelpFormatter)

    # define los comandos (mutuamente excluyentes)
    commands = parser.add_argument_group('Comandos')
    commands = commands.add_mutually_exclusive_group(required=True)
    commands.add_argument('-h', '--help', action='store_true', help='Muestra esta ayuda y termina')
    commands.add_argument('-v', '--version', action='version', help='Mostrar versión', version=f'%(prog)s {__project_version__}')
    commands.add_argument('--search', action='store_true', help='Buscar empresas')

    # define las opciones adicionales a los comandos
    options = parser.add_argument_group('Opciones')
    options.add_argument('--category', metavar='CATEGORY', nargs='?', help='Categoría de las empresas a buscar')
    options.add_argument('--location', metavar='LOCATION', nargs='?', help='Ubicación para la búsqueda de empresas')
    options.add_argument('--radius', metavar='RADIUS', nargs='?', help='Radio en kilómetros para la búsqueda', default=5.0, type=float)
    options.add_argument('--output', metavar='OUTPUT', nargs='?', help='Fichero de salida en formato CSV')

    # parsea los argumentos
    args = parser.parse_args()

    # lógica según las opciones
    if args.help:
        parser.print_help()
        return

    start_time = time.time()

    if args.search:

        print(f"Buscando empresas de la categoría '{args.category}' en '{args.location}' con un radio de {args.radius} km...")

        # Obtiene la clave de la API de Google Places
        apikey = os.getenv("GOOGLE_PLACES_API_KEY")

        # Crea una instancia de la API de Google Places
        api = PlacesAPI(apikey)

        # Realiza la búsqueda de empresas
        places = api.search(args.category, args.location, args.radius)

        if args.output:
            # Guardar los resultados en un fichero CSV
            save_csv(places, args.output)
            # Mostrar mensaje de confirmación
            print(f"Resultados guardados en '{args.output}'")
        else:
            # Convertir objetos en una lista de listas
            places_data = [
                [
                    shorten(place.name, width=40, placeholder="..."), 
                    place.type, 
                    shorten(place.address, width=40, placeholder="..."), 
                    place.phone, 
                    place.website
                ] for place in places
            ]
            # Mostrar la tabla con encabezados
            print(tabulate(places_data, headers=["Nombre", "Tipo", "Dirección", "Teléfono", "Web"], tablefmt="grid"))

    print(f"Tiempo transcurrido: {time.time() - start_time:.2f} s")

if __name__ == "__main__":
    main()

