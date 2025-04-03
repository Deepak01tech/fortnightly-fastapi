from sqlalchemy.orm import Session
from ..import schemas,database,models
from fastapi import status,HTTPException


def create_user(request:schemas.User,db: Session):
    new_user = models.User(
        email=request.email,
        password=request.password,
        created_at=request.created_at,  # ✅ Now included
        updated_at=request.updated_at
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "data": new_user}

def show(id:int,db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user