from pydantic import BaseModel, EmailStr, Field
from typing import List
from app.schemas.blogs import BlogResponse  

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserRequeste(UserBase):
    pass
class UserResponse(UserBase):
    id: int
    name: str
    email: EmailStr
    blogs: List[BlogResponse] = Field(default_factory=list)

    class Config:
        orm_attribute = True