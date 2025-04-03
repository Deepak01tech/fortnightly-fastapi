from sqlalchemy.orm import Session
from ..import schemas,database,models
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException



def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db: Session):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        created_at=request.created_at,  # ✅ Now included
        updated_at=request.updated_at
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"message": "Blog post created", "data": new_blog}

def delete(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Blog post deleted"}

def update(id:int,request:schemas.Blog,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.title = request.title
    blog.body = request.body
    blog.created_at = request.created_at  # ✅ Now included
    blog.updated_at = request.updated_at
    db.commit()
    db.refresh(blog)
    return {"message": "Blog post updated", "data": blog}

def show(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog