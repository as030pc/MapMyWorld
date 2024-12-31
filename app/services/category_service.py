from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate
from fastapi import HTTPException

class CategoryService:
    """
    Servicio para manejar las operaciones relacionadas con las categorías.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el servicio con una sesión de base de datos.

        Parámetros:
            db (Session): Sesión de la base de datos.
        """
        self.db = db

    def get_all_categories(self):
        """
        Obtener todas las categorías de la base de datos.
        """
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int):
        """
        Obtener una categoría específica por su ID.
        """
        return self.db.query(Category).filter(Category.id == category_id).first()

    def create_category(self, category_data: CategoryCreate):
        """
        Crear una nueva categoría en la base de datos.
        """
        existing_category = self.db.query(Category).filter(
            Category.name == category_data.name
        ).first()

        if existing_category:
            raise HTTPException(status_code=400, detail="La categoría ya existe")

        new_category = Category(**category_data.dict())
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    def delete_category(self, category_id: int):
        """
        Eliminar una categoría de la base de datos.
        """
        category = self.get_category_by_id(category_id)
        if category:
            self.db.delete(category)
            self.db.commit()
        return category
