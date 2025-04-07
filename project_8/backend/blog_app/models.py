from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)  # Assuming this is a foreign key to a User table
    created_at = Column(String(50), nullable=False)  # Store date as string for simplicity

    updated_at = Column(String(50), nullable=True)  # Store date as string for simplicity
    is_deleted = Column(Integer, default=0)  # 0 for not deleted, 1 for deleted
    deleted_at = Column(String(50), nullable=True)  # Store date as string for simplicity

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    blog_id = Column(Integer, nullable=False)  # Assuming this is a foreign key to a Blog table
    user_id = Column(Integer, nullable=False)  # Assuming this is a foreign key to a User table
    comment_text = Column(Text, nullable=False)
    created_at = Column(String(50), nullable=False)  # Store date as string for simplicity

    updated_at = Column(String(50), nullable=True)  # Store date as string for simplicity
    is_deleted = Column(Integer, default=0)  # 0 for not deleted, 1 for deleted
    deleted_at = Column(String(50), nullable=True)  # Store date as string for simplicity

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  # Store hashed password
    created_at = Column(String(50), nullable=False)  # Store date as string for simplicity

    updated_at = Column(String(50), nullable=True)  # Store date as string for simplicity
    is_deleted = Column(Integer, default=0)  # 0 for not deleted, 1 for deleted
    deleted_at = Column(String(50), nullable=True)  # Store date as string for simplicity