from fastapi import APIRouter, Depends, HTTPException
from app.data import database
from app.api import user
from app import schema
from app.data import models
router = APIRouter()

@router.get("/users")
def get_users():
    return user.get_users_from_db()

@router.post("/")
def add_user(user: schema.User_create):
    try:
        models.create_users_table_if_not_exists()
        return models.insert_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))