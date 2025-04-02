from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List
from passlib.context import CryptContext
from datetime import datetime

router = APIRouter(
    tags=["User"],
)
get_db = database.get_db


@router.post("/user")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashedPassword = CryptContext(schemes=["bcrypt"],deprecated="auto").hash(request.password)
    new_user = User(
        name=request.name,
        email=request.email,
        password=hashedPassword,
        created_at=request.created_at,

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request