import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Category
from app.services.category_service import CategoryService

# Configuración de la base de datos en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas en la base de datos de prueba
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

def test_get_all_categories(db_session):
    # Crear una instancia del servicio de categorías
    category_service = CategoryService(db_session)
    
    # Agregar categorías de prueba a la base de datos
    db_session.add(Category(name="Category 1"))
    db_session.add(Category(name="Category 2"))
    db_session.commit()
    
    # Obtener todas las categorías
    categories = category_service.get_all_categories()
    
    # Verificar que se obtuvieron las categorías correctamente
    assert len(categories) == 2
    assert categories[0].name == "Category 1"
    assert categories[1].name == "Category 2"