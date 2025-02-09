import requests

from bf.latlng import LatLng
from bf.place import Place

class PlacesAPI:

    # URL base de la API de Google Places (New)
    BASE_URL = "https://places.googleapis.com/v1/places"

    # Clave de la API de Google Places
    apikey : str = None

    def __init__(self, apikey: str):
        self.apikey = apikey

    def __get_headers(self, fieldMask : list[str]) -> dict:
        """
        Genera los encabezados de la solicitud.
        """
        return {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.apikey,              # Clave de la API
            "X-Goog-FieldMask": ",".join(fieldMask)     # Máscara de campos (https://developers.google.com/maps/documentation/places/web-service/text-search?hl=es-419#fieldmask)
        }

    def locate(self, address: str) -> LatLng:
        """
        Obtiene la ubicación geográfica de una dirección.
        - address: Dirección a geolocal
        """

        # URL de la API de Google Places (New)
        url = f"{self.BASE_URL}:searchText"

        # Encabezados de la solicitud
        headers = self.__get_headers([ "places.location" ])

        # Cuerpo de la solicitud en formato JSON
        payload = {
            "textQuery": address
        }

        # Realizar la solicitud POST
        response = requests.post(url, json=payload, headers=headers)

        # Procesar la respuesta
        if response.status_code == 200:
            location = response.json().get("places", [{}])[0].get("location", {})
            return LatLng(location.get("latitude", 0), location.get("longitude", 0))
        else:
            print("Error en la solicitud:", response.text)
            return LatLng(0, 0)

    def search(self, category: str, locationText: str, radius: float) -> list[Place]:
        """
        Busca empresas en una ubicación geográfica.
        - category: Categoría de las empresas a buscar.
        - locationText: Ubicación para la búsqueda de empresas.
        - radius: Radio en kilómetros para la búsqueda centrada en la ubicación especificada en locationText.
        """

        # Busca la ubicación geográfica de la dirección (latitud y longitud), por ejemplo: "Calle Castillo, Santa Cruz de Tenerife"
        latlng = self.locate(locationText)

        # URL de la API de Google Places (New)
        url = f"{self.BASE_URL}:searchText?rankPreference=DISTANCE"

        # Encabezados de la solicitud
        fieldMask = [
            "places.displayName", 
            "places.formattedAddress", 
            "places.businessStatus", 
            "places.primaryTypeDisplayName", 
            "places.regularOpeningHours", 
            "places.nationalPhoneNumber", 
            "places.googleMapsLinks", 
            "places.websiteUri" 
        ]
        headers = self.__get_headers(fieldMask)

        # Cuerpo de la solicitud en formato JSON
        payload = {
            "textQuery": category,
            "languageCode": "es",
            "regionCode": "ES",
            "locationBias": {
                "circle": {
                    "center": {
                        "latitude": latlng.latitude,
                        "longitude": latlng.longitude
                    },
                    "radius": float(radius) * 1000
                }
            }
        }

        # Realizar la solicitud POST
        response = requests.post(url, json=payload, headers=headers)

        # Procesar la respuesta
        if response.status_code == 200:
            places = response.json().get("places", [])
            placesList = []
            for place in places:
                placesList.append(Place(place))
            return placesList
        else:
            raise Exception("Error en la solicitud:", response.text)

