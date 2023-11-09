"""Database session."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    url=settings.database_uri,
    pool_size=int(settings.pool_size),
    max_overflow=int(settings.max_overflow),
    pool_timeout=float(settings.pool_timeout),
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
