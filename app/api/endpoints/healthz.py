"""Healthcheck endpoint for the API."""

from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """Send a GET request to the route & hopes to get a "200" response code."""
    return {"healthz": "OK"}
