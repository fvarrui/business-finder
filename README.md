# Business Finder

![Versión](https://img.shields.io/badge/Versión-0.2.0-black)

Aplicación Python que busca información de empresas en el servicio web [Places API](https://developers.google.com/maps/documentation/places) de Google.

> Útil para encontrar empresas de prácticas para estudiantes.

## ¿Qué hace?

La función principal de **Business Finder** es buscar empresas en el servicio web Places API de Google. La búsqueda se realiza por categorías de empresas (palabras clave) en un radio de kilómetros determinado alrededor de la ubicación especificada.

## ¿Cómo se usa?

Para buscar empresas, se debe utilizar el comando `bf` desde un terminal. 

Por ejemplo, para buscar empresas de informática en Santa Cruz de Tenerife en un radio de 5 km:

```bash
$ bf --search --category informática --location "Santa Cruz de Tenerife" --radius 5
```

> Si no se especifica fichero de salida con las opciones `--excel` o `--csv`, los resultados se mostrarán por pantalla.

Para obtener ayuda sobre cómo usar el script, se puede utilizar la opción `--help`:

```bash
$ bf --help

Uso: bf (-h | -v | --search) [--category CATEGORY] [--location LOCATION] [--latlng LATLNG] [--radius RADIUS] [--csv [OUTPUT]] [--excel [OUTPUT]] [--apikey KEY]

Buscador de empresas chupiguay (v0.2.0)

Comandos:
  -h, --help           Muestra esta ayuda y termina
  -v, --version        Mostrar versión
  --search             Buscar empresas

Opciones:
  --category CATEGORY  Categoría de las empresas a buscar
  --location LOCATION  Ubicación para la búsqueda de empresas (p.ej. "Santa Cruz de Tenerife, España")
  --latlng LATLNG      Ubicación para la búsqueda de empresas en formato "latitud,longitud"
  --radius RADIUS      Radio en kilómetros para la búsqueda
  --csv [OUTPUT]       Fichero de salida en formato CSV
  --excel [OUTPUT]     Fichero de salida en formato XLSX
  --apikey KEY         Clave de API de Google Places (si no se especifica, se buscará en las variables de entorno)

¡Corre, que te las quita el César!
```

Ejemplo:

```bash
$ bf --search --category "software" --location "silicon valley, california" --radius 5

Buscando empresas de la categoría 'software' en 'silicon valley, california' con un radio de 5.0 km...
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Nombre                                  | Tipo          | Dirección                                | Teléfono       | Web                               |
+=========================================+===============+==========================================+================+===================================+
| 360Logica Software Testing Services...  | No disponible | 640 W California Ave #210, Sunnyvale,... | (773) 649-5838 | http://www.360logica.com/         |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Aera Technology                         | No disponible | 707 California St, Mountain View, CA...  | (408) 524-2222 | http://www.aeratechnology.com/    |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Algoworks Solutions Inc                 | No disponible | 355 W Olive Ave #204, Sunnyvale, CA...   | (877) 284-1028 | https://www.algoworks.com/        |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Atlassian                               | No disponible | 301 E Evelyn Ave, Mountain View, CA...   | (415) 701-1110 | https://www.atlassian.com/        |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Bdna Corporation                        | No disponible | 339 N Bernardo Ave # 206, Mountain...    | (650) 625-9530 | http://www.bdna.com/              |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Bloomreach, Inc.                        | No disponible | 700 E El Camino Real #130, Mountain...   | No disponible  | http://bloomreach.com/            |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Calfus                                  | No disponible | 415 Clyde Ave Ste 103, Mountain View,... | (925) 558-0312 | https://www.calfus.com/           |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| CARIAD, Inc.                            | No disponible | 450 National Ave, Mountain View, CA...   | No disponible  | http://cariad.us/                 |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Circ                                    | No disponible | 967 N Shoreline Blvd, Mountain View,...  | (650) 265-4460 | No disponible                     |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Contextual AI, Inc.                     | No disponible | 150 W Evelyn Ave #200, Mountain View,... | No disponible  | https://contextual.ai/            |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
+ [...]                                                                                                                                                   +
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Software Development | Mobile Apps      | No disponible | 220 N Mathilda Ave Apt 61, Sunnyvale,... | (262) 788-8070 | https://i2techs.com/              |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| StarTree Inc                            | No disponible | 100 View St UNIT 204, Mountain View,...  | No disponible  | https://www.startree.ai/          |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Syllable Ai Corporation                 | No disponible | 800 W El Camino Real Suite 275,...       | No disponible  | https://syllable.ai/              |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Tekton Labs Inc                         | No disponible | 800 W El Camino Real #180, Mountain...   | (650) 267-4703 | http://www.tektonlabs.com/        |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| ThorDrive                               | No disponible | 144 S Whisman Rd #C, Mountain View,...   | No disponible  | https://www.thordrive.ai/         |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Unravel Data                            | No disponible | 319 N Bernardo Ave, Mountain View, CA... | (650) 741-3442 | https://www.unraveldata.com/      |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Velocity Software Inc                   | No disponible | 196 Castro St, Mountain View, CA...      | (650) 964-8867 | http://www.velocity-software.com/ |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Veloxy                                  | No disponible | 1240 Dale Ave Suite#5, Mountain View,... | (510) 402-6913 | https://veloxy.io/                |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| VergeSense                              | No disponible | 153 Castro St, Mountain View, CA...      | (617) 618-5006 | https://vergesense.com/           |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
| Zettaset, Inc.                          | No disponible | 465 Fairchild Dr #234, Mountain View,... | (650) 314-7920 | http://www.zettaset.com/          |
+-----------------------------------------+---------------+------------------------------------------+----------------+-----------------------------------+
Se encontraron 60 empresas
Tiempo transcurrido: 2.81 s
```

## ¿Qué se necesita?

Para poder utilizar **Business Finder** se necesita una clave de API de Google Places API. 

Para más información sobre cómo [obtener una clave de API de Google Places API](https://console.cloud.google.com/google/maps-apis/credentials) visita la [documentación de Google](https://developers.google.com/maps/documentation/places/web-service/get-api-key).

Es posible especificar la API KEY cuando se ejecuta `bf` con la opción `--apikey`. Si no se especifica, se buscará en la variable de entorno `GOOGLE_PLACES_API_KEY`, que puedes definir de la siguiente manera:

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

Si ya has instalado alguna versión de `business-finder`, puedes actualizarlo con el siguiente comando:

```bash
pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/fvarrui/business-finder.git
```

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

--- 

Made with ❤️ by [fvarrui](https://github.com/fvarrui)