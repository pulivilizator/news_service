from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Path

from core import dto
from services.news_service import NewsService

router = APIRouter(route_class=DishkaRoute, prefix='/news')

@router.get(path='/{user_id}/for-hour/',
            response_model=list[dto.NewsItem])
async def get_news_for_hour(
        user_id: Annotated[int, Path()],
        news_service: FromDishka[NewsService]
):
    news = await news_service.get_for_hour(user_id=user_id)
    return news

@router.get(path='/{user_id}/for-day/',
            response_model=list[dto.NewsItem])
async def get_news_for_day(
        user_id: Annotated[int, Path()],
        news_service: FromDishka[NewsService]
):
    news = await news_service.get_for_day(user_id=user_id)
    return news