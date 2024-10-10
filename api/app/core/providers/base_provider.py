from typing import AsyncIterator

from aiohttp import ClientSession
from dishka import Provider, provide, Scope
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config.config import get_config, ConfigModel


class BaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> ConfigModel:
        return get_config()

    @provide(scope=Scope.APP)
    async def get_sessionmaker(self, config: ConfigModel) -> async_sessionmaker:
        engine = create_async_engine(url=config.db.dsn.unicode_string())
        return async_sessionmaker(engine, expire_on_commit=False, autoflush=True)

    @provide(scope=Scope.REQUEST)
    async def get_db_session(self, sessionmaker: async_sessionmaker) -> AsyncIterator[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    @provide(scope=Scope.APP)
    async def get_redis(self, config: ConfigModel) -> AsyncIterator[Redis]:
        r = Redis.from_url(config.redis.dsn.unicode_string())
        yield r
        await r.aclose()

    @provide(scope=Scope.REQUEST)
    async def get_client_session(self) -> AsyncIterator[ClientSession]:
        async with ClientSession() as session:
            yield session


