import pytest
from fastapi.testclient import TestClient
from  app.main import app

client = TestClient(app)

def test_read_locations():
    response = client.get("/locations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_location():
    response = client.post("/locations", json={"name": "New Location", "latitude": 40.7128, "longitude": -74.0060})
    assert response.status_code == 201
    assert response.json()["name"] == "New Location"

def test_read_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_category():
    response = client.post("/categories", json={"name": "New Category"})
    assert response.status_code == 201
    assert response.json()["name"] == "New Category"

def test_read_recommendations():
    response = client.get("/location-category-reviews")
    assert response.status_code == 200
    assert isinstance(response.json(), list)