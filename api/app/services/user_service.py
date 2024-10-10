from core import dto
from repository.implementations.user_repository import UserRepository
from services.base import AbstractService


class UserService(AbstractService):
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def create_user(self, data: dto.UserRegister) -> dto.User:
        user = await self._repository.create(data)
        return user

    async def get_user(self, user_id: int) -> dto.User | None:
        user = await self._repository.retrieve(user_id, raise_for_none=False)
        return user