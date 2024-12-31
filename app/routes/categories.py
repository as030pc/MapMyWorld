from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CategoryCreate, CategoryResponse
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    """
    Obtener todas las categorías.
    """
    service = CategoryService(db)
    return service.get_all_categories()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """
    Obtener una categoría específica por su ID.
    """
    service = CategoryService(db)
    category = service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva categoría.
    """
    service = CategoryService(db)
    return service.create_category(category)


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una categoría por su ID.
    """
    service = CategoryService(db)
    deleted_category = service.delete_category(category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
