from pydantic import BaseModel
from datetime import datetime

class Blog(BaseModel):
    title: str
    body: str
    created_at: datetime = datetime.utcnow()  # ✅ Default timestamp
    updated_at: datetime = datetime.utcnow()  # ✅ Default timestamp

    # ✅ Needed for SQLAlchemy model conversion

class ShowBlog(BaseModel):
    title: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
    created_at: datetime = datetime.utcnow()  # ✅ Default timestamp
