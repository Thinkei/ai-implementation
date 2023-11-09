"""Endpoints for documents ingestion and conversation."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/")
def say_greeting() -> dict[str, str]:
    """Say greeting."""
    return {"greeting": "Hello !"}
