from fastapi import FastAPI, Depends,status,Response
from sqlalchemy.orm import Session
from blog import schemas
from blog.models import Blog,User ,Base# ✅ Correct import
from blog.database import engine, SessionLocal
from passlib.context import CryptContext
from .routers import blog,user # ✅ Correct import

app = FastAPI()
Base.metadata.create_all(bind=engine)  # ✅ Create tables in the database

app.include_router(blog.router)  # ✅ Include the router
app.include_router(user.router)  # ✅ Include the user router
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

