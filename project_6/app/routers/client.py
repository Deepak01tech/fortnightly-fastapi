from app.api import client
from fastapi import APIRouter, Depends, status
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import ClientCreate, ClientResponse


router = APIRouter(
    prefix="/client",
    tags=["Client"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
def add_client(client_data: ClientCreate,user_id: int, db: Session = Depends(get_db) ):
    return client.create_client(db, client_data, user_id)
