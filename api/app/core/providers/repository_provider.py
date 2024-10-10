from dishka import Provider, provide, Scope
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from core import dto
from core.config.config import ConfigModel
from repository import models
from repository.implementations import UserRepository, SourceRepository
from repository.interfaces.redis_repository import RedisRepository


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(session=session,
                              model=models.User,
                              dto_model=dto.User,
                              lookup_field='user_id')

    @provide(scope=Scope.REQUEST)
    def get_source_repository(self, session: AsyncSession) -> SourceRepository:
        return SourceRepository(session=session,
                                model=models.Source,
                                dto_model=dto.Source,
                                lookup_field='source_id')

    @provide(scope=Scope.APP)
    async def get_redis_repository(self, r: Redis) -> RedisRepository:
        return RedisRepository(r=r)