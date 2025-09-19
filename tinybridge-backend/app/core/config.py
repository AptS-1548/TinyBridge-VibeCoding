import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tinybridge.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")