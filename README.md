# Map My World

## Descripción
Map My World es una API REST desarrollada con FastAPI para gestionar ubicaciones y categorías, permitiendo a los usuarios explorar y revisar combinaciones de ubicaciones y categorías. Además, incluye un recomendador que sugiere combinaciones que no han sido revisadas recientemente.

---

## Requisitos
- Python 3.8+
- SQLite (base de datos por defecto)
- Docker (opcional para despliegue)
- Alembic (para migraciones de base de datos)

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
$ git clone https://github.com/as030pc/MapMyWorld.git
```

### 2. Crear un entorno virtual (opcional pero recomendado)
```bash
$ python -m venv venv
$ source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
$ pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```env
DATABASE_URL=sqlite:///./map_my_world.db
```

### 5. Inicializar la base de datos
Utiliza Alembic para generar la estructura inicial de la base de datos:
```bash
$ alembic upgrade head
```

---

## Estructura del Proyecto
```plaintext
map_my_world/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── locations.py
│   │   ├── categories.py
│   │   ├── location_category_reviews.py
│   ├── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── location_service.py
│   │   ├── category_service.py
│   │   ├── location_category_review_service.py
├── alembic/  # Directorio generado por Alembic
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
└── requirements.txt
```

---

## Uso

### Ejecutar localmente

1. Activa tu entorno virtual si no está activo.
2. Realizar las migraciones para la creacion de la db en SQLite:
   ```bash
   $ alembic upgrade head
   ``` 
3. Inicia la aplicación:
   ```bash
   $ uvicorn app.main:app --reload
   ```
4. Abre tu navegador en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para explorar la documentación interactiva de la API.

### Usar Docker

1. Construye y ejecuta los contenedores:
   ```bash
   $ docker-compose up --build
   ```
2. Accede a la aplicación en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Endpoints Principales

### Ubicaciones (`/locations`)
- **GET** `/locations`: Obtiene todas las ubicaciones.
- **POST** `/locations`: Crea una nueva ubicación.
- **GET** `/locations/{id}`: Obtiene una ubicación por ID.
- **PUT** `/locations/{id}`: Actualiza una ubicación existente.
- **DELETE** `/locations/{id}`: Elimina una ubicación.

### Categorías (`/categories`)
- **GET** `/categories`: Obtiene todas las categorías.
- **POST** `/categories`: Crea una nueva categoría.
- **GET** `/categories/{id}`: Obtiene una categoría por ID.
- **PUT** `/categories/{id}`: Actualiza una categoría existente.
- **DELETE** `/categories/{id}`: Elimina una categoría.

### Revisiones de Ubicación-Categoría (`/recomendations`)
- **GET** `/recommendations`: Obtiene recomendaciones de exploración.
- **POST** `/recommendations`: Crea una nueva revisión de ubicación-categoría.

---

## Configuración de Alembic

### Archivo `alembic.ini`
Asegúrate de que la variable `sqlalchemy.url` apunta a tu base de datos:
```ini
sqlalchemy.url = sqlite:///./map_my_world.db
```

### Inicializar Alembic
```bash
$ alembic init migrations
```

### Crear una migración
```bash
$ alembic revision --autogenerate -m "mensaje de migración"
```

### Aplicar migraciones
```bash
$ alembic upgrade head
```

---

## Acceso a Swagger

Puedes acceder a la documentación interactiva de la API generada automáticamente por Swagger en la siguiente URL:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Alternativamente, puedes usar la interfaz de Redoc en:

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Correr Test Unitarios
Usa el siguiente comando para correr los test
```bash
$ pytest
```




