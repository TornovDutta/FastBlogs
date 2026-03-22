from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.core.database import Base

class users(Base):
    __tablename__="users"

    id=Column(Integer,index=True,primary_key=True)
    name=Column(String)
    email=Column(String)

    bolgs=relationship("Blog", back_populates="owner", cascade="all, delete")