from pydantic import BaseModel, EmailStr
from typing import Optional


# ====================
# User Schemas
# ====================
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None
    is_deleted: int
    deleted_at: Optional[str] = None

    class Config:
        orm_mode = True


# ====================
# Blog Schemas
# ====================
class BlogBase(BaseModel):
    title: str
    body: str
    author_id: int

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None
    is_deleted: int
    deleted_at: Optional[str] = None

    class Config:
        orm_mode = True


# ====================
# Comment Schemas
# ====================
class CommentBase(BaseModel):
    blog_id: int
    user_id: int
    comment_text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None
    is_deleted: int
    deleted_at: Optional[str] = None

    class Config:
        orm_mode = True
