import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from app.api.api import api_router
from app.middlewares.i18n_middleware import I18nMiddleware
from app.db.session import Base

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    debug=True
)

app.include_router(api_router)
app.add_middleware(I18nMiddleware)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
