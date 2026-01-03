import os
from pydantic_settings import BaseSettings
 

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./dev.db")
    BEELINE_REPO_URL: str = "https://github.com/Murali-group/Beeline"
    DATA_DIR: str = "data/"
    CLONE_DIR: str = "beeline_repo/"

    class Config:
        env_file = ".env"

settings = Settings()
