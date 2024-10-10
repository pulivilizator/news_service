import asyncio

from dishka import make_async_container
from dishka.integrations.taskiq import setup_dishka, inject, FromDishka
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import RedisAsyncResultBackend, ListQueueBroker

from core.providers import get_providers
from services import SourceService
from services.news_service import NewsService
from core.config.config import get_config

config = get_config()

redis_async_result = RedisAsyncResultBackend(
    redis_url=config.redis.dsn.unicode_string(),
)

broker = ListQueueBroker(
    url=config.redis.dsn.unicode_string(),
).with_result_backend(result_backend=redis_async_result)

container = make_async_container(*get_providers())
setup_dishka(container=container, broker=broker)

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


@broker.task(schedule=[{"cron": "*/1 * * * *"}])
@inject
async def task(source_service: FromDishka[SourceService],
               news_service: FromDishka[NewsService]):
    urls = await source_service.get_all()
    await asyncio.gather(*[
        news_service.parse_source(url.url, user_id=url.user_id) for url in urls
    ])