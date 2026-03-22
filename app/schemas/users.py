from pydantic import BaseModel, EmailStr, Field
from typing import List
from app.schemas.blogs import BlogResponse  

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    blogs: List[BlogResponse] = Field(default_factory=list)

    class Config:
        from_attributes = True