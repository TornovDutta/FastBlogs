from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserResponse
from app.crud import users as crud_user
from app.dependencies.dataabase import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)