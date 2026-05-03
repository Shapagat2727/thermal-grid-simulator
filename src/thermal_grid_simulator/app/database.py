from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

DB_USER = os.getenv("DB_USER", "testuser")  # Default to 'testuser' if not set
DB_PASSWORD = os.getenv("DB_PASSWORD", "testpassword")  # Default to 'testpassword' if not set
DB_HOST = os.getenv("DB_HOST", "localhost")  # Default to 'localhost' if not set
DB_PORT = os.getenv("DB_PORT", 5432)  # Default to 5432 if not set
DB_NAME = os.getenv("DB_NAME", "thermal_db")  # Default to 'thermal_db' if not set
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()