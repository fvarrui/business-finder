# Business Finder

Aplicación Python que busca información de empresas en el servicio web [Places API](https://developers.google.com/maps/documentation/places) de Google.

> Útil para encontrar empresas de prácticas para estudiantes.

## ¿Qué hace?

La función principal de **Business Finder** es buscar empresas en el servicio web Places API de Google. La búsqueda se realiza por categorías de empresas (palabras clave) en un radio de kilómetros determinado alrededor de la ubicación especificada.

## ¿Cómo se usa?

Para buscar empresas, se debe utilizar el script `bf` desde la línea de comandos. Por ejemplo, para buscar empresas de informática en Santa Cruz de Tenerife en un radio de 5 km:

```bash
$ bf --search --category informática --location "Santa Cruz de Tenerife" --radius 5
```

> Si no se especifica fichero de salida con la opción `--output`, los resultados se mostrarán por pantalla.

Para obtener ayuda sobre cómo usar el script, se puede utilizar la opción `--help`:

```bash
$ bf --help

Uso: bf (-h | -v | --search) [--category [CATEGORY]] [--location [LOCATION]] [--radius [RADIUS]] [--output [OUTPUT]]

Buscador de empresas

Comandos:
  -h, --help            Muestra esta ayuda y termina
  -v, --version         Mostrar versión
  --search              Buscar empresas

Opciones:
  --category [CATEGORY]
                        Categoría de las empresas a buscar
  --location [LOCATION]
                        Ubicación para la búsqueda de empresas
  --radius [RADIUS]     Radio en kilómetros para la búsqueda
  --output [OUTPUT]     Fichero de salida en formato CSV

¡Ahora ponte a buscar empresas!
```

## ¿Qué se necesita?

Para poder utilizar **Business Finder** se necesita una clave de API de Google Places API. Esta clave se debe especificar en la variable de entorno `GOOGLE_PLACES_API_KEY`:

> Para obtener una clave de API de Google Places API, visita la [documentación de Google](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

### Linux 

```bash
$ export GOOGLE_PLACES_API_KEY="tu_clave_de_api"
```

### Windows (PowerShell)

```powershell
PS> $env:GOOGLE_PLACES_API_KEY = "tu_clave_de_api"
```

### Windows (CMD)

```cmd
C:\> set GOOGLE_PLACES_API_KEY=tu_clave_de_api
```

## ¿Cómo se instala?

Para instalar **Business Finder** en tu sistema, puedes hacerlo desde el repositorio de GitHub con el comando `pip` (debes ejecutarlo como Administrador en Windows o con `sudo` en Linux):

```bash
pip install git+https://github.com/fvarrui/business-finder.git
```

> Por supuesto, debes tener Python instalado en tu sistema.

## Para desarrolladores

Si quieres colaborar en el desarrollo de **Business Finder**, puedes hacerlo de la siguiente manera.

Clonar el repositorio y entrar en el directorio:

```bash
git clone https://github.com/fvarrui/business-finder.git
cd business-finder
```

Crear un entorno virtual (si no lo hemos hecho antes):

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
venv\Scripts\activate
```

Instalar el paquete en modo de edición, de modo que se crearán los scripts del paquete y se instalarán las dependencias en el entorno virtual:

```bash
pip install -e .
```

¡Y a programar!

```bash
code .
```

## ¿Cómo contribuir?

¡Tus PRs son bienvenidos!