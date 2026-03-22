from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str

class BlogRequeste(BaseModel):
    pass


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_attribute = True