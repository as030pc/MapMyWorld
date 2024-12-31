from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import LocationCreate, LocationResponse
from app.services.location_service import LocationService

router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)

@router.get("/", response_model=list[LocationResponse])
def get_all_locations(db: Session = Depends(get_db)):
    """
    Obtener todas las ubicaciones.
    """
    service = LocationService(db)
    return service.get_all_locations()

@router.get("/{location_id}", response_model=LocationResponse)
def get_location(location_id: int, db: Session = Depends(get_db)):
    """
    Obtener una ubicación específica por su ID.
    """
    service = LocationService(db)
    location = service.get_location_by_id(location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.post("/", response_model=LocationResponse)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva ubicación.
    """
    service = LocationService(db)
    return service.create_location(location)

@router.put("/{location_id}", response_model=LocationResponse)
def update_location(location_id: int, location: LocationCreate, db: Session = Depends(get_db)):
    """
    Actualizar una ubicación existente.
    """
    service = LocationService(db)
    updated_location = service.update_location(location_id, location)
    if not updated_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated_location

@router.delete("/{location_id}", response_model=LocationResponse)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una ubicación.
    """
    service = LocationService(db)
    deleted_location = service.delete_location(location_id)
    if not deleted_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return deleted_location