from abc import ABC, abstractmethod
from typing import Type

from aiohttp import ClientSession
from pydantic import BaseModel
from typing_extensions import TypeVar

from core.config.config import ConfigModel

ResponseModel = TypeVar('ResponseModel', bound=BaseModel)

class AbstractService(ABC):
    @abstractmethod
    def __init__(self,
                 session: ClientSession,
                 base_url: str):
        raise NotImplementedError

    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

class BaseService(AbstractService):
    def __init__(self,
                 session: ClientSession,
                 base_url: str):
        self._session = session
        self._base_url = base_url

    async def create(self,
                     path: str,
                     data: BaseModel,
                     response_model: Type[ResponseModel] | None = None) -> ResponseModel | None:
        url = f'{self._base_url}{path}'
        async with self._session.post(url=url,
                                      json=data.model_dump(mode='json')) as response:
            return (response.status if response_model is None
                                    else response_model.model_validate(await response.json(), from_attributes=True))

    async def get(self, path: str, response_model: Type[ResponseModel]) -> ResponseModel:
        url = f'{self._base_url}{path}'
        async with self._session.get(url=url) as response:
            response.raise_for_status()
            data = await response.json()
            return response_model.model_validate(data, from_attributes=True)