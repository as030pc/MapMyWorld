from sqlalchemy.orm import Session
from app.models import Location
from app.schemas import LocationCreate
from fastapi import HTTPException
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
        if  not location_data.latitude or not location_data.longitude:
            raise HTTPException(status_code=400, detail="Faltan campos requeridos")
        if not (-90 <= location_data.latitude <= 90):
            raise HTTPException(status_code=400, detail="Latitud no válida")
        if not (-180 <= location_data.longitude <= 180):
            raise HTTPException(status_code=400, detail="Longitud no válida")

        
        existing_location = self.db.query(Location).filter(
            Location.latitude == location_data.latitude,
            Location.longitude == location_data.longitude
        ).first()

        if existing_location:
            raise HTTPException(status_code=400, detail="La ubicación ya existe")

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