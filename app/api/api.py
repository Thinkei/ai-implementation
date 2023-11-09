"""All API Routers."""

from fastapi import APIRouter
from app.api.endpoints import (
    healthz,
)
from app.api.v1.endpoints import (
    test
)

from app.core.config import settings

api_router = APIRouter()

# Healthz
api_router.include_router(healthz.router, prefix="/healthz", tags=["healthz"])

# API V1
api_router.include_router(
    test.router,
    prefix=f"{settings.api_v1_prefix}/test",
    tags=["test"],
)