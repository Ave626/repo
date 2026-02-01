from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import Literal
from functools import lru_cache

class Settings(BaseSettings):
    app_name : str = "MyApp"
    enviroment: Literal["development","testing","production"] = "development"
    database_url : str = "sqlite:///./local.db"
    secret_key: str = "super_insecure_default_key"
    model_config = SettingsConfigDict(
        env_file=".env",             
        env_file_encoding="utf-8"     
    )

@lru_cache()
def get_settings()-> Settings:
    return Settings()