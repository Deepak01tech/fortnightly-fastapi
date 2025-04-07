from fastapi import APIRouter, HTTPException
from app import schema
from app.api import user as user_service  # renamed to avoid conflict
from app.data import models

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@router.post("/")
def add_user(new_user: schema.User_create):
    try:
        models.create_users_table_if_not_exists()
        return models.insert_user(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_users():
    try:
        return user_service.get_users_from_db()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}")
def get_user(user_id: int):
    try:
        result = user_service.get_user_by_id(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{user_id}")
def update_user(user_id: int, updated_user: schema.User_create):
    try:
        return user_service.update_user(user_id, updated_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        return user_service.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# This code defines a FastAPI router for user-related operations.
# It includes endpoints to add, get, update, and delete users.
# The router uses the user_service module to interact with the database and handle user data.
# Each endpoint has error handling to return appropriate HTTP status codes in case of exceptions.
# The router is prefixed with "/user" and tagged with "User" for better organization in the API documentation.