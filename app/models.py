from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    location_categories = relationship("LocationCategoryReviewed", back_populates="location")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_categories = relationship("LocationCategoryReviewed", back_populates="category")


class LocationCategoryReviewed(Base):
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
