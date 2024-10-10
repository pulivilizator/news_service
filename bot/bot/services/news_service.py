from aiohttp import ClientSession

from core import dto
from core.enums import NewsForTime
from services.base import AbstractService, BaseService


class NewsService(BaseService):
    async def get_news_for_time(self, time: NewsForTime, user_id: int) -> list[dto.NewsItem]:
        url = f'{self._base_url}news/{user_id}/for-{time}'
        async with self._session.get(url=url) as response:
            response.raise_for_status()
            news = await response.json()
            return [dto.NewsItem.model_validate(item, from_attributes=True) for item in news]