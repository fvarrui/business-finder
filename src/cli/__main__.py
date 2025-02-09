import os
import time
import argparse

from bf.__init__ import __module__, __project_description__, __project_version__
from bf.placesapi import PlacesAPI

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

    start_time = time.time()

    # lógica según las opciones
    if args.help:
        parser.print_help()
        return
    
    if args.search:
        print(f"Buscando empresas de la categoría '{args.category}' en '{args.location}' con un radio de {args.radius} km...")
        # gets the api key from the environment
        apikey = os.getenv("GOOGLE_PLACES_API_KEY")
        # creates an instance of the PlacesAPI class
        api = PlacesAPI(apikey)
        # performs the business search
        api.search(args.category, args.location, args.radius)

    print(f"Elapsed time: {time.time() - start_time:.2f} s")

if __name__ == "__main__":
    main()

