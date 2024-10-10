from sqlalchemy import select

from core import dto
from repository.implementations.source_repository import SourceRepository
from repository.models import Source, User
from .base import AbstractService


class SourceService(AbstractService):
    def __init__(self, repository: SourceRepository):
        self._repository = repository

    async def create_source(self, data: dto.CreateSource) -> dto.Source:
        source = await self._repository.create(model_data=data)
        return source

    async def get_all(self) -> list[dto.Source]:
        sources = await self._repository.list()
        return sources