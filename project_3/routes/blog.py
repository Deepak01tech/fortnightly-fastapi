from fastapi import APIRouter, HTTPException

from api.schemas import Blog
from api.db import blog_db, blog_id_counter

router = APIRouter()

@router.post("/blog")
def create_blog(request: Blog):
    global blog_id_counter
    blog = {
        "id": blog_id_counter,
        "title": request.title,
        "body": request.body
    }
    blog_db.append(blog)
    blog_id_counter += 1

    return {"message": " created successfully","blog":blog}

@router.get("/blog/{id}")
def get_blog():
    return {"blogs": blog_db}

@router.get("/blog/{id}")
def get_blog(id: int):
    for blog in blog_db:
        if blog["id"] == id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/blog/{id}")
def update_blog(id: int, request: Blog):
    for blog in blog_db:
        if blog["id"] == id:
            blog["title"] = request.title
            blog["body"] = request.body
            return {"message": "Blog updated successfully", "blog": blog}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/blog/{id}")
def delete_blog(id: int):
    for blog in blog_db:
        if blog["id"] == id:
            blog_db.remove(blog)
            return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")
