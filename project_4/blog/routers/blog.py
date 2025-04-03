from fastapi import APIRouter,Depends,status

from ..import schemas,database,models
from typing import List, Optional
from sqlalchemy.orm import Session

from ..api import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)
get_db = database.get_db

@router.get("/",response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):

    return blog.get_all(db)


@router.post("/}",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request,db)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(database.get_db)):
    return blog.destroy(id,db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id,request,db)

@router.get("/{id}",response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(database.get_db)):
    return blog.show(id,db)

