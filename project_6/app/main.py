from fastapi import FastAPI, Depends, status, Response
from app.routers import client, project,user  # ✅ Correct import
from pydantic import BaseModel
from .database import Base, engine

app = FastAPI()

app.include_router(client.router)  # ✅ Include the router
app.include_router(project.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)

@app.get("/hello")
async def root():
    return {"message": "Hello, World!"}

print("FastAPI app initialized successfully.")

