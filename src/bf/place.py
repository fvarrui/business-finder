class Place:

    def __init__(self, json: dict):
        self.name = json.get('displayName', {}).get('text', 'Desconocido')
        self.address = json.get('formattedAddress', 'No disponible')
        self.status = json.get('businessStatus', 'No disponible')
        self.phone = json.get('nationalPhoneNumber', 'No disponible')
        self.website = json.get('websiteUri', 'No disponible')
        self.timetable = json.get('regularOpeningHours', { 'weekDayDescriptions': [] }).get('weekdayDescriptions')
        self.mapLink = json.get('googleMapsLinks', { 'placeUri': 'No disponible' }).get('placeUri')
        self.type = json.get('primaryTypeDisplayName', { 'text': 'No disponible' }).get('text')

    def __str__(self):
        return f"{self.name} ({self.type}): {self.address} - {self.status} - {self.phone} - {self.website}"