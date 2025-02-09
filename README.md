# Business Finder

Aplicación Python que busca información de empresas por categorías en los servicios de [Here](https://here.com) y [Yelp](https://yelp.com).

## ¿Qué hace?

La función principal de `business-finder` es buscar empresas para la categoría especificada en los servicios de Here y Yelp. La búsqueda se realiza en un radio de 15 km alrededor de la ubicación especificada.

## ¿Cómo se usa?

Para buscar empresas, se puede utilizar el script `business_finder.py` desde la línea de comandos. Por ejemplo, para buscar restaurantes en Madrid:

```bash
business_finder --category technology --location "Santa Cruz de Tenerife, Spain"
```


## Información para desarrolladores

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
