from fastapi import APIRouter, HTTPException
from app import schema
from app.data import models

router = APIRouter()

@router.post("/project")
def add_project(project: schema.ProjectCreate):
    try:
        models.create_projects_table_if_not_exists()
        return models.insert_project(project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
