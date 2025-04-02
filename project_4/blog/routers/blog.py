from fastapi import APIRouter,Depends,status

from ..import schemas,database,models
from typing import List, Optional
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Blog"],
)
get_db = database.get_db
@router.get("/blog",response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
