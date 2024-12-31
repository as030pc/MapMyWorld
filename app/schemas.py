from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class LocationCreate(BaseModel):
    latitude: float = Field(..., description="Latitud de la ubicación", example=40.7128)
    longitude: float = Field(..., description="Longitud de la ubicación", example=-74.0060)


class LocationResponse(LocationCreate):
    id: int = Field(..., description="ID único de la ubicación")

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str = Field(..., description="Nombre de la categoría", example="Restaurantes")


class CategoryResponse(CategoryCreate):
    id: int = Field(..., description="ID único de la categoría")

    class Config:
        orm_mode = True


class LocationCategoryReviewed(BaseModel):
    location_id: int = Field(..., description="ID de la ubicación")
    category_id: int = Field(..., description="ID de la categoría")
    reviewed_at: Optional[str] = Field(None, description="Fecha de la última revisión")

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str = Field(..., description="Nombre de la categoría", example="Restaurantes")


class CategoryResponse(CategoryCreate):
    id: int = Field(..., description="ID único de la categoría")

    class Config:
        orm_mode = True


class LocationCategoryReviewResponse(BaseModel):
    category_name: str
    location_id: int
    category_id: int
    location_coordinates: str
    last_reviewed_at: str | None

    class Config:
        orm_mode = True


class LocationCategoryReviewCreate(BaseModel):
    location_id: int
    category_id: int

    class Config:
        orm_mode = True
