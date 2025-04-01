from fastapi import APIRouter
from api import schemas  

router = APIRouter()

@router.post("/blog")
def create_blog(request: schemas.Blog):
    return {"message": f"Blog '{request.title}' created successfully"}
