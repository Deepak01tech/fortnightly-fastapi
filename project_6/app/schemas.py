from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ClientCreate(BaseModel):
    client_name: str

class ClientResponse(ClientCreate):
    id: int
    created_at: datetime
    created_by: int

class ProjectCreate(BaseModel):
    project_name: str
    client_id: int

class ProjectResponse(ProjectCreate):
    id: int
    created_by: int
