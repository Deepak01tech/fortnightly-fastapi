from fastapi import FastAPI, Depends,status,Response
from sqlalchemy.orm import Session
from blog import schemas
from blog.models import Blog,User ,Base# ✅ Correct import
from blog.database import engine, SessionLocal
from passlib.context import CryptContext
from routers import blog,user # ✅ Correct import

app = FastAPI()
Base.metadata.create_all(bind=engine)  # ✅ Create tables in the database

app.include_router(blog.router)  # ✅ Include the router
app.include_router(user.router)  # ✅ Include the user router
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog_post(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = Blog(
        title=request.title,
        body=request.body,
        created_at=request.created_at,  # ✅ Now included
        updated_at=request.updated_at
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {"message": "Blog post created", "data": new_blog}

@app.delete("/blog/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        return {"error": "Blog post not found"}
    db.delete(blog)
    db.commit()
    return {"message": "Blog post deleted"}


@app.put("/blog/{blog_id}", status_code=status.HTTP_200_OK)
def update_blog(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        return {"error": "Blog post not found"}

    blog.title = request.title
    blog.body = request.body
    blog.created_at = request.created_at  # ✅ Now included
    blog.updated_at = request.updated_at

    db.commit()
    db.refresh(blog)

    return {"message": "Blog post updated", "data": blog}




@app.get("/blog/{blog_id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def get_blog(blog_id: int,response:Response, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Blog post not found"}
    return blog



