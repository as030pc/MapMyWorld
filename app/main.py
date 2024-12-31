from fastapi import FastAPI
from .database import Base, engine
from .routes import locations, categories, locations_categories


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Map My World API")


app.include_router(locations.router)
app.include_router(categories.router)
app.include_router(locations_categories.router)
