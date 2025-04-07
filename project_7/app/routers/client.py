from fastapi import APIRouter, HTTPException
from app import schema
from app.data import models

router = APIRouter()

@router.post("/client")
def add_client(client: schema.ClientCreate):
    try:
        models.create_clients_table_if_not_exists()
        return models.insert_client(client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
