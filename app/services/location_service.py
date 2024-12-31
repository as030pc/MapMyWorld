from sqlalchemy.orm import Session
from app.models import Location
from app.schemas import LocationCreate

class LocationService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_locations(self):
        """
        Obtener todas las ubicaciones de la base de datos.
        """
        return self.db.query(Location).all()

    def get_location_by_id(self, location_id: int):
        """
        Obtener una ubicación específica por su ID.
        """
        return self.db.query(Location).filter(Location.id == location_id).first()

    def create_location(self, location_data: LocationCreate):
        """
        Crear una nueva ubicación en la base de datos.
        """
        new_location = Location(**location_data.dict())
        self.db.add(new_location)
        self.db.commit()
        self.db.refresh(new_location)
        return new_location

    def update_location(self, location_id: int, location_data: LocationCreate):
        """
        Actualizar una ubicación existente.
        """
        location = self.get_location_by_id(location_id)
        if location:
            for key, value in location_data.dict().items():
                setattr(location, key, value)
            self.db.commit()
            self.db.refresh(location)
        return location

    def delete_location(self, location_id: int):
        """
        Eliminar una ubicación de la base de datos.
        """
        location = self.get_location_by_id(location_id)
        if location:
            self.db.delete(location)
            self.db.commit()
        return location