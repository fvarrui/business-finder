
class LatLng:
    latitude : float = None
    longitude : float = None

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.latitude},{self.longitude}"