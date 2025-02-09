class Place:

    def __init__(self, json: dict):
        self.name = json.get('displayName', {}).get('text', 'Desconocido')
        self.address = json.get('formattedAddress', 'No disponible')
        self.status = json.get('businessStatus', 'No disponible')
        self.phone = json.get('nationalPhoneNumber', 'No disponible')
        self.website = json.get('websiteUri', 'No disponible')
        type = json.get('primaryTypeDisplayName')
        if type is None:
            self.type = 'No disponible'
        else:
            self.type = type.get('text', 'Desconocido')

    def __str__(self):
        return f"{self.name} ({self.type}): {self.address} - {self.status} - {self.phone} - {self.website}"