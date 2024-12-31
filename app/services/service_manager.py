from .location_service import LocationService


class ServiceManager:
    def __init__(self, db):
        self.location_service = LocationService(db)