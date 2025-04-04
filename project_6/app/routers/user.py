from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import UserCreate
from app.api import user


router = APIRouter(
    prefix="/user",
    tags=["User"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db,user_data)