from dishka import Provider

from .base_provider import BaseProvider
from .repository_providers import RepositoryProvider
from .service_provider import ServiceProvider


def get_providers() -> list[Provider]:
    return [
        BaseProvider(),
        RepositoryProvider(),
        ServiceProvider(),
    ]