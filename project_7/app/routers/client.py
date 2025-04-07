from fastapi import APIRouter, HTTPException
from app import schema
from app.api import client as client_service  # avoid name conflict
from app.data import models

router = APIRouter(
    prefix="/client",
    tags=["Client"]
)

@router.post("/")
def add_client(new_client: schema.ClientCreate):
    try:
        models.create_clients_table_if_not_exists()
        return models.insert_client(new_client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_clients():
    try:
        return client_service.get_all_clients()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{client_id}")
def get_client(client_id: int):
    try:
        result = client_service.get_client_by_id(client_id)
        if not result:
            raise HTTPException(status_code=404, detail="Client not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{client_id}")
def update_client(client_id: int, updated_client: schema.ClientCreate):
    try:
        return client_service.update_client(client_id, updated_client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{client_id}")
def delete_client(client_id: int):
    try:
        return client_service.delete_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# This code defines a FastAPI router for client-related operations.
# It includes endpoints to add, get, update, and delete clients.
# The router uses the client_service module to interact with the database and handle client data.
# Each endpoint has error handling to return appropriate HTTP status codes in case of exceptions.

