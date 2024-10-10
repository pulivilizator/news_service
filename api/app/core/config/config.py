from environs import Env
from pydantic import BaseModel

from core.config.models import RedisConfig, DB


class ConfigModel(BaseModel):
    redis: RedisConfig
    db: DB

def get_config(path: str = None) -> ConfigModel:
    env = Env()
    env.read_env(path)

    return ConfigModel(
        redis=RedisConfig(
            dsn='redis://' + env.str('REDIS_DSN')
        ),
        db=DB(
            dsn=env.str('POSTGRES_DSN')
        )
    )