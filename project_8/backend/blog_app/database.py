from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace with your actual MySQL credentials
USERNAME = "root"
PASSWORD = "deepak"
HOST = "localhost"
PORT = "3306"
DB_NAME = "blog_db"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:deepak@localhost:3306/blog_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
