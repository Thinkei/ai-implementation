"""Core configuration."""

import logging
import os
import pathlib

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # Base
    api_v1_prefix: str = os.getenv("API_V1_PREFIX", "/api/v1")
    debug: bool = os.getenv("DEBUG", "True")
    project_name: str = os.getenv("PROJECT_NAME", "AI Implementation")
    version: str = os.getenv("VERSION", "0.1.0")
    description: str = os.getenv("DESCRIPTION", "AI Implementation")

    # Database
    db_user: str = os.getenv("DB_USER", "ai_implementation")
    db_password: str = os.getenv("DB_PASSWORD", "ai_implementation")
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: str = os.getenv("DB_PORT", "5431")
    db_name: str = os.getenv("DB_NAME", "ai_implementation")
    pool_size: str = os.getenv("DATABASE_POOL_SIZE", "5")
    max_overflow: str = os.getenv("DATABASE_MAX_OVERFLOW", "10")
    pool_timeout: str = os.getenv("DATABASE_POOL_TIMEOUT", "30.0")
    database_uri: str = os.getenv(
        "DATABASE_URL",
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
    )

    # Open AI
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
