from ..api import project as project_api
from fastapi import APIRouter, Depends, status
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import ProjectCreate, ProjectResponse

router = APIRouter(
    prefix="/project",
    tags=["Project"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def add_project(project: ProjectCreate, user_id: int, db: Session = Depends(get_db)):
    return project_api.create_project(db, project, user_id)
