import asyncio
from datetime import datetime, timedelta

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from xml.etree import ElementTree as ET

from core import dto
from repository.interfaces.redis_repository import RedisRepository
from services.base import AbstractService



class NewsService(AbstractService):
    SUPPORTED_TAGS = ['b', 'strong', 'i', 'em', 'u', 's', 'a', 'code', 'pre']

    def __init__(self, repository: RedisRepository, session: ClientSession):
        self._repository = repository
        self._session = session
        self._ua = UserAgent()
        self._ex_time = 86400 #1 день

    async def get_for_hour(self, user_id: int):
        one_hour_ago = int((datetime.now() - timedelta(hours=1)).timestamp())
        all_keys = [key.decode('utf-8') for key in await self._repository.r.keys(f'news:{user_id}:*')]

        keys_for_hour = []
        for key in all_keys:
            timestamp = int(float(key.split(':')[2]))
            if timestamp > one_hour_ago:
                keys_for_hour.append(key)

        raw_news = await asyncio.gather(
            *[
                self._repository.get(key)
                for key in keys_for_hour
            ]
        )

        news = [dto.NewsItem.model_validate_json(item) for item in raw_news]
        news.sort(key=lambda x: x.pub_date, reverse=True)
        return news

    async def get_for_day(self, user_id: int):
        keys = [key.decode('utf-8') for key in await self._repository.r.keys(f'news:{user_id}:*')]
        raw_news = await asyncio.gather(
            *[
                self._repository.get(key)
                for key in keys
            ]
        )

        news = [dto.NewsItem.model_validate_json(item) for item in raw_news]

        news.sort(key=lambda x: x.pub_date, reverse=True)
        return news

    async def parse_source(self, source, user_id):
        async with self._session.get(source, headers={'User-Agent': self._ua.random}) as response:
            response.raise_for_status()
            items = []
            content = await response.text()
            root = ET.fromstring(content)
            for item in root.findall('.//item'):
                title = item.find('title').text
                link = item.find('link').text
                description = item.find('description')
                if description is not None:
                    description = self._remove_unsupported_tags(description.text)
                category = item.find('category')
                if category is not None:
                    category = category.text
                pub_date_str = ' '.join(item.find('pubDate').text.split(' ')[:-1])
                pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S")

                news_item = dto.NewsItem(title=title, link=link, description=description, category=category,
                                     pub_date=pub_date)
                items.append(news_item)
            await asyncio.gather(
                *[
                    self._repository.set_ex(name=f'news:{user_id}:{news_item.pub_date.timestamp()}:{news_item.link}',
                          value=news_item.model_dump_json(), time=self._ex_time)
                    for news_item in items
                ]
            )

    def _remove_unsupported_tags(self, text):
        if text is None:
            return
        soup = BeautifulSoup(text, "html.parser")

        for tag in soup.find_all(True):
            if tag.name not in self.SUPPORTED_TAGS:
                tag.unwrap()

        return str(soup)