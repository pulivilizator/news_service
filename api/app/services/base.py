from abc import ABC, abstractmethod

from repository.interfaces.base import AbstractSQLRepository


class AbstractService(ABC):
    @abstractmethod
    def __init__(self, repository: AbstractSQLRepository):
        raise NotImplementedError