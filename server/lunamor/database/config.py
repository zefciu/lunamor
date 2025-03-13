from pydantic_settings import BaseSettings

class DatabaseConfiguration(BaseSettings):
    DATABASE_URL: str


def get_db_config() -> DatabaseConfiguration:
    return DatabaseConfiguration()
