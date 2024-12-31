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
    Obtener recomendaciones de exploración.

    Retorna hasta 10 combinaciones de ubicación y categoría que no han sido revisadas
    en los últimos 30 días, priorizando aquellas que nunca han sido revisadas.

    Parámetros:
        limit (int): Número máximo de recomendaciones a devolver. Por defecto es 10.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        list[LocationCategoryReviewResponse]: Lista de recomendaciones de exploración.
    """
    service = LocationCategoryReviewService(db)
    return service.get_exploration_recommendations(limit)


@router.post("/", status_code=201)
def add_location_category_review(
    review_data: LocationCategoryReviewCreate, db: Session = Depends(get_db)
):
    """
    Crear una nueva revisión de ubicación-categoría.

    Parámetros:
        review (LocationCategoryReviewCreate): Datos de la nueva revisión.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        LocationCategoryReviewResponse: La revisión creada.
    """
    service = LocationCategoryReviewService(db)
    return service.create_location_category_review(review_data)
