from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import Settings
engine=create_engine(Settings.DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine,autoflush=True,autoCommit=True)
Base=declarative_base()