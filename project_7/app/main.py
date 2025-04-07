from fastapi import FastAPI
from app.routers import user,client,project
from app.data import models
app= FastAPI()

models.create_users_table_if_not_exists()
app.include_router(user.router)
app.include_router(client.router)
app.include_router(project.router)

@app.get("/")
def read_root():
    return {"API IS STARTED"}