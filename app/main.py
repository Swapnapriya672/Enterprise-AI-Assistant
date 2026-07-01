from fastapi import FastAPI

from app.api.routes import router as query_router
from app.api.health import router as health_router

from app.config.settings import (
    HOST,
    PORT,
)


app = FastAPI(

    title="Enterprise AI Assistant",

    version="1.0.0"
)

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    query_router,
    prefix="/api/v1",
    tags=["Enterprise AI"]
)


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "app.main:app",

        host=HOST,

        port=PORT,

        reload=True
    )