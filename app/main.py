from fastapi import FastAPI
from app.core.database import sessionmaker,Base,engine


app=FastAPI(title="blogsApplications")
Base.metadata.create_all(bind=engine)