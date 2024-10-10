from pathlib import Path

from environs import Env
from pydantic import BaseModel, HttpUrl

from core.config.models import RedisConfig, BotConfig

BASE_DIR = Path(__file__).parent.parent.parent

class ConfigModel(BaseModel):
    redis: RedisConfig
    bot: BotConfig
    api_url: HttpUrl

def get_config(path: str = None) -> ConfigModel:
    env = Env()
    env.read_env(path)

    return ConfigModel(
        redis=RedisConfig(
            dsn='redis://' + env.str('REDIS_STORAGE_DSN')
        ),
        bot=BotConfig(
            token=env.str('BOT_TOKEN')
        ),
        api_url=env.str('API_URL')
    )