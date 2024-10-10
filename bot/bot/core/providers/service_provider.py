from aiohttp import ClientSession
from dishka import Provider, provide, Scope

from core.config.config import ConfigModel
from services.news_service import NewsService
from services.source_service import SourceService
from services.user_service import UserService


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_service(self, session: ClientSession, config: ConfigModel) -> UserService:
        return UserService(session=session, base_url=config.api_url)

    @provide(scope=Scope.REQUEST)
    def get_source_service(self, session: ClientSession, config: ConfigModel) -> SourceService:
        return SourceService(session=session, base_url=config.api_url)

    @provide(scope=Scope.REQUEST)
    def get_news_service(self, session: ClientSession, config: ConfigModel) -> NewsService:
        return NewsService(session=session, base_url=config.api_url)

