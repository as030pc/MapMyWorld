import pytest
from fastapi.testclient import TestClient
from tests.test_config import client


def test_create_location_invalid_latitude(client: TestClient):
    response = client.post("/locations/", json={"name": "Invalid Latitude", "latitude": 100.0, "longitude": 90.0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Latitud no válida"

def test_create_location_invalid_longitude(client: TestClient):
    response = client.post("/locations/", json={"name": "Invalid Longitude", "latitude": 45.0, "longitude": 200.0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Longitud no válida"

