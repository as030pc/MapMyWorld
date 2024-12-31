import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./map_my_world.db") 