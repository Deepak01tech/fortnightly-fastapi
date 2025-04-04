from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(255))

    projects = relationship("Project", back_populates="creator")
    clients = relationship("Client", back_populates="creator")

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(100), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="clients")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    created_by = Column(Integer, ForeignKey("users.id"))


    creator = relationship("User", back_populates="projects")