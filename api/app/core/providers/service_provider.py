from aiohttp import ClientSession
from dishka import Provider, provide, Scope

from repository.implementations import SourceRepository, UserRepository
from repository.interfaces.redis_repository import RedisRepository
from services import UserService, SourceService
from services.news_service import NewsService


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_service(self, repository: UserRepository) -> UserService:
        return UserService(repository=repository)

    @provide(scope=Scope.REQUEST)
    def get_source_service(self, repository: SourceRepository) -> SourceService:
        return SourceService(repository=repository)

    @provide(scope=Scope.REQUEST)
    def get_news_service(self, session: ClientSession, repository: RedisRepository) -> NewsService:
        return NewsService(session=session, repository=repository)