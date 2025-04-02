from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of database.py
DB_PATH = os.path.join(BASE_DIR, "..", "blog.db")  # Correct relative path
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"
engine= create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
