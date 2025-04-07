from pydantic import BaseModel

class User_create(BaseModel):
    username: str
    email: str
    password: str



class ClientCreate(BaseModel):
    client_name: str
    created_by: int


class ProjectCreate(BaseModel):
    project_name: str
    client_id: int
    created_by: int