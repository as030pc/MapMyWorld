from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Location(Base):
    """
    Modelo de la tabla 'locations' en la base de datos.

    Atributos:
        id (int): Identificador único de la ubicación.
        name (str): Nombre de la ubicación.
        latitude (float): Latitud de la ubicación.
        longitude (float): Longitud de la ubicación.
        created_at (datetime): Fecha y hora de creación de la ubicación.
        location_categories (relationship): Relación con la tabla 'location_categories_reviewed'.
    """
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    location_categories = relationship("LocationCategoryReviewed", back_populates="location")


class Category(Base):
    """
    Modelo de la tabla 'categories' en la base de datos.

    Atributos:
        id (int): Identificador único de la categoría.
        name (str): Nombre de la categoría.
        location_categories (relationship): Relación con la tabla 'location_categories_reviewed'.
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_categories = relationship("LocationCategoryReviewed", back_populates="category")


class LocationCategoryReviewed(Base):
    """
    Modelo de la tabla 'location_categories_reviewed' en la base de datos.

    Atributos:
        id (int): Identificador único de la relación.
        location_id (int): Identificador de la ubicación.
        category_id (int): Identificador de la categoría.
        reviewed_at (datetime): Fecha y hora de la última revisión.
        location (relationship): Relación con la tabla 'locations'.
        category (relationship): Relación con la tabla 'categories'.
    """
    __tablename__ = "location_category_reviewed"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    location_id = Column(
        Integer, ForeignKey("locations.id"), nullable=False
    ) 
    category_id = Column(
        Integer, ForeignKey("categories.id"), nullable=False
    ) 
    reviewed_at = Column(DateTime, default=None) 
    location = relationship("Location", back_populates="location_categories")
    category = relationship("Category", back_populates="location_categories")
