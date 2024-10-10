from enum import StrEnum, IntEnum


class BaseKeys(StrEnum):
    WIDGET_KEY: str
    REDIS_KEY: str

class Language(BaseKeys):
    RU = 'ru'
    EN = 'en'

    WIDGET_KEY = 'language'
    REDIS_KEY = 'language:{}'

class ApiUrls(StrEnum):
    REGISTER = 'user/registration/'
    USER = 'user/{}/'

    SOURCE = 'sources/'

    NEWS_FOR_HOUR = 'news/{}/for-hour/'
    NEWS_FOR_DAY = 'news/{}/for-day/'

class NewsForTime(StrEnum):
    DAY = 'day'
    HOUR = 'hour'