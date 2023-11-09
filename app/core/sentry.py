"""Sentry configuration."""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Sentry(BaseSettings):
    """Sentry setting for the application."""

    sentry_dsn: str = ""
    sentry_environment: str = os.getenv("ENVIRONMENT", "")
    sentry_traces_sample_rate: str = ""


sentry = Sentry()