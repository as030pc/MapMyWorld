from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.location_categories_service import LocationCategoryReviewService
from app.database import get_db
from app.schemas import LocationCategoryReviewCreate, LocationCategoryReviewResponse


router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/", summary="Get exploration recommendations", response_model=list[LocationCategoryReviewResponse])
def get_recommendations(limit: int = 10, db: Session = Depends(get_db)):
    """
    Returns up to 10 location-category combinations that haven't been reviewed
    in the last 30 days, prioritizing those that have never been reviewed.
    """
    service = LocationCategoryReviewService(db)
    return service.get_exploration_recommendations(limit)


@router.post("/", status_code=201)
def add_location_category_review(
    review_data: LocationCategoryReviewCreate, db: Session = Depends(get_db)
):
    """
    Add a new location-category review entry.
    Validates the existence of location and category, and prevents duplicates.
    """
    service = LocationCategoryReviewService(db)
    return service.create_location_category_review(review_data)
