
from app.schemas import ClientCreate
from sqlalchemy.orm import Session
from app.models import Client






def create_client(db:Session, client: ClientCreate,user_id:int):

    db_client = Client(client_name=client.client_name, created_by=user_id)  # Assuming created_by is set to 1 for now
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client




