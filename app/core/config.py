from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./database.db"

    model_config = {
        "env_file": ".env"
    }

settings = Settings()