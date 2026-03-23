from sqlalchemy.orm import session 
from app import models

def get_users(db:session):
    return db.query(models.users).all()