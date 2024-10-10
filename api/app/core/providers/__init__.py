from dishka import Provider

from .base_provider import BaseProvider
from .service_provider import ServiceProvider
from .repository_provider import RepositoryProvider


def get_providers() -> list[Provider]:
    return [
        BaseProvider(),
        RepositoryProvider(),
        ServiceProvider(),
    ]