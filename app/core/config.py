from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str="sqlite:///./database.db"
    
    class Config:
        evn_file=".env"
Setting=Settings()

