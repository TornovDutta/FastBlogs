from fastapi import FastAPI
from app.core.database import sessionmaker,Base,engine
from app.api.v1.router import api_router

app=FastAPI(title="blogsApplications")
Base.metadata.create_all(bind=engine)
app.include_router(api_router,prefix="/api/v1")