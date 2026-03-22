from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class BLogs(Base):
    __tablename__="blogs"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)

    user_id=Column(Integer,ForeignKey("users.id"))

    owner = relationship("User", back_populates="blogs")