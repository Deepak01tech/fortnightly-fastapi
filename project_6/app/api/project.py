from  app.models import Project
from app.schemas import ProjectCreate
from sqlalchemy.orm import Session


def create_project(db: Session, project: ProjectCreate, user_id: int):
    db_project = Project(
        project_name=project.project_name,
        client_id=project.client_id,
        created_by=user_id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
