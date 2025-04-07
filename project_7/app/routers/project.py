from fastapi import APIRouter, HTTPException
from app import schema
from app.api import project as project_service  # avoid name conflict
from app.data import models

router = APIRouter(
    prefix="/project",
    tags=["Project"],
)

@router.post("/")
def add_project(new_project: schema.ProjectCreate):
    try:
        models.create_projects_table_if_not_exists()
        return models.insert_project(new_project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_projects():
    try:
        return project_service.get_all_projects()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{project_id}")
def get_project(project_id: int):
    try:
        result = project_service.get_project_by_id(project_id)
        if not result:
            raise HTTPException(status_code=404, detail="Project not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{project_id}")
def update_project(project_id: int, updated_project: schema.ProjectCreate):
    try:
        return project_service.update_project(project_id, updated_project)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{project_id}")
def delete_project(project_id: int):
    try:
        return project_service.delete_project(project_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# This code defines a FastAPI router for project-related operations.
# It includes endpoints to add, get, update, and delete projects.
# The router uses the project_service module to interact with the database and handle project data.
# Each endpoint has error handling to return appropriate HTTP status codes in case of exceptions.
# The router is prefixed with "/project" and tagged with "Project" for better organization in the API documentation.
# This code is part of a larger FastAPI application that manages users, clients, and projects.
