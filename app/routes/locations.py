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

    Parámetros:
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        list[LocationResponse]: Lista de todas las ubicaciones.
    """
    service = LocationService(db)
    return service.get_all_locations()

@router.get("/{location_id}", response_model=LocationResponse)
def get_location(location_id: int, db: Session = Depends(get_db)):
    """
    Obtener una ubicación específica por su ID.

    Parámetros:
        location_id (int): Identificador único de la ubicación.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        LocationResponse: La ubicación correspondiente al ID proporcionado.

    Lanza:
        HTTPException: Si la ubicación no se encuentra.
    """
    service = LocationService(db)
    location = service.get_location_by_id(location_id)
    if not location:
        raise HTTPException(status_code=404, detail="ubicacion no encontrada")
    return location

@router.post("/", response_model=LocationResponse)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva ubicación.

    Parámetros:
        location (LocationCreate): Datos de la nueva ubicación.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        LocationResponse: La ubicación creada.
    """
    service = LocationService(db)
    return service.create_location(location)

@router.put("/{location_id}", response_model=LocationResponse)
def update_location(location_id: int, location: LocationCreate, db: Session = Depends(get_db)):
    """
    Actualizar una ubicación existente.

    Parámetros:
        location_id (int): Identificador único de la ubicación a actualizar.
        location (LocationCreate): Datos actualizados de la ubicación.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        LocationResponse: La ubicación actualizada.

    Lanza:
        HTTPException: Si la ubicación no se encuentra.
    """
    service = LocationService(db)
    updated_location = service.update_location(location_id, location)
    if not updated_location:
        raise HTTPException(status_code=404, detail="Ubicacion no encontrada")
    return updated_location

@router.delete("/{location_id}", response_model=LocationResponse)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una ubicación por su ID.

    Parámetros:
        location_id (int): Identificador único de la ubicación a eliminar.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        LocationResponse: La ubicación eliminada.

    Lanza:
        HTTPException: Si la ubicación no se encuentra.
    """
    service = LocationService(db)
    deleted_location = service.delete_location(location_id)
    if not deleted_location:
        raise HTTPException(status_code=404, detail="Ubicacion no encontrada")
    return deleted_location