from pydantic_settings import BaseSettings

class DatabaseConfiguration(BaseSettings):
    DATABASE_URL: str
