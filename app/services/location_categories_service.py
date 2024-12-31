from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import LocationCategoryReviewed, Location, Category
from app.schemas import LocationCategoryReviewCreate
from fastapi import HTTPException


class LocationCategoryReviewService:
    def __init__(self, db: Session):
        self.db = db

    def get_exploration_recommendations(self, limit: int = 10):
        """
        Obtener recomendaciones de exploración con combinaciones de ubicación y categoría
        que no han sido revisadas en los últimos 30 días, priorizando las nunca revisadas.
        """
        cutoff_date = datetime.utcnow() - timedelta(seconds=30)

        recommendations = (
            self.db.query(LocationCategoryReviewed)
            .filter(
                or_(
                    LocationCategoryReviewed.reviewed_at.is_(None),
                    LocationCategoryReviewed.reviewed_at < cutoff_date,
                )
            )
            .order_by(
                LocationCategoryReviewed.reviewed_at.is_(None).desc(),
                LocationCategoryReviewed.reviewed_at.asc(),
            )
            .limit(limit)
            .all()
        )

        for item in recommendations:
            item.reviewed_at = datetime.utcnow()
            self.db.add(item)

        self.db.commit()

        return [
            {
                "location_id": item.location_id,
                "category_id": item.category_id,
                "location_coordinates": f"( latitud:{item.location.latitude}, longitud: {item.location.longitude})",
                "category_name": item.category.name,
                "last_reviewed_at": (
                    item.reviewed_at.strftime("%d-%m-%Y %H:%M:%S")
                    if item.reviewed_at
                    else "Nunca revisada"
                ),
            }
            for item in recommendations
        ]

    def create_location_category_review(self, review_data: LocationCategoryReviewCreate):
        """
        Crear una nueva relación de revisión entre ubicación y categoría.
        """

        location = self.db.query(Location).filter(Location.id == review_data.location_id).first()
        if not location:
            raise HTTPException(
                status_code=404, detail=f"Location with ID {review_data.location_id} not found"
            )

        category = self.db.query(Category).filter(Category.id == review_data.category_id).first()
        if not category:
            raise HTTPException(
                status_code=404, detail=f"Category with ID {review_data.category_id} not found"
            )

        existing_review = (
            self.db.query(LocationCategoryReviewed)
            .filter(
                LocationCategoryReviewed.location_id == review_data.location_id,
                LocationCategoryReviewed.category_id == review_data.category_id,
            )
            .first()
        )
        if existing_review:
            raise HTTPException(
                status_code=400,
                detail="This location-category combination already exists",
            )

        new_review = LocationCategoryReviewed(**review_data.dict())
        try:
            self.db.add(new_review)
            self.db.commit()
            self.db.refresh(new_review)
            return new_review
        except Exception as e:
            self.db.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"An error occurred while creating the location-category review: {e}",
            )
