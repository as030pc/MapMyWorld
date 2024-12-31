import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import LocationCreate, CategoryCreate
from app.services.location_service import LocationService
from app.services.category_service import CategoryService
from tests.test_config import db




def test_create_location_invalid_latitude(db: Session):
    service = LocationService(db)
    location_data = LocationCreate(name="Invalid Latitude", latitude=100.0, longitude=90.0)
    
    with pytest.raises(HTTPException) as excinfo:
        service.create_location(location_data)
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Latitud no válida"

def test_create_location_invalid_longitude(db: Session):
    service = LocationService(db)
    location_data = LocationCreate(name="Invalid Longitude", latitude=45.0, longitude=200.0)
    
    with pytest.raises(HTTPException) as excinfo:
        service.create_location(location_data)
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Longitud no válida"

