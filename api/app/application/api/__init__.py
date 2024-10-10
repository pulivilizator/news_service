from fastapi import APIRouter
from .users import router as users_router
from .sources import router as sources_router
from .news import router as news_router

def get_routers() -> list[APIRouter]:
    return [
        users_router,
        sources_router,
        news_router
    ]