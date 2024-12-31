from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CategoryCreate, CategoryResponse
from app.services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    """
    Modelo de la tabla 'categories' en la base de datos.

    Atributos:
        id (int): Identificador único de la categoría.
        name (str): Nombre de la categoría.
        location_categories (relationship): Relación con la tabla 'location_categories_reviewed'.
    """
    service = CategoryService(db)
    return service.get_all_categories()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """
    Obtener una categoría específica por su ID.

    Parámetros:
        category_id (int): Identificador único de la categoría.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        CategoryResponse: La categoría correspondiente al ID proporcionado.
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

    Parámetros:
        category (CategoryCreate): Datos de la nueva categoría.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        CategoryResponse: La categoría creada.
    """
    service = CategoryService(db)
    return service.create_category(category)


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """
    Eliminar una categoría por su ID.

    Parámetros:
        category_id (int): Identificador único de la categoría a eliminar.
        db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
        CategoryResponse: La categoría eliminada.
    """
    service = CategoryService(db)
    deleted_category = service.delete_category(category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
