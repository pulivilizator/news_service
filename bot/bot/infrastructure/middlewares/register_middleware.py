from http import HTTPStatus
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject
from aiohttp import ClientResponseError
from dishka.integrations.aiogram import FromDishka
from fluentogram import TranslatorHub
from redis.asyncio import Redis

from core import dto
from core.enums import Language, ApiUrls
from repository.implementations.bot_repository import BotRepository
from services.user_service import UserService
from .inject_middleware import aiogram_middleware_inject


class RegisterMiddleware(BaseMiddleware):
    @aiogram_middleware_inject
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
            repository: FromDishka[BotRepository],
            service: FromDishka[UserService],
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        if not await repository.exists(Language.REDIS_KEY.format(user.id)):
            try:
                has_user = await service.get(path=ApiUrls.USER.format(user.id), response_model=dto.User)
            except ClientResponseError as e:
                if e.status == HTTPStatus.NOT_FOUND:
                    has_user = None
                else:
                    raise e
            if  has_user is None:
                new_user = dto.RegisterUser(user_id=user.id,
                                           first_name=user.first_name,
                                           last_name=user.last_name)

                await service.create(data=new_user, path=ApiUrls.REGISTER)
            await repository.set(Language.REDIS_KEY.format(user.id), Language.RU)

        return await handler(event, data)