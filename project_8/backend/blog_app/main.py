from fastapi import FastAPI
from . import models, database
from blog_app.routers import blog, user, comment

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Blog App")

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(comment.router, prefix="/comment", tags=["comment"])


