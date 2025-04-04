from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URI = "mysql://root:deepak@localhost:3306/project_management_db"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()  # ✅ No engine argument
metadata.bind = engine  # ✅ Explicitly bind engine if needed
