from pydantic import BaseModel, RedisDsn, PostgresDsn


class RedisConfig(BaseModel):
    dsn: RedisDsn

class DB(BaseModel):
    dsn: PostgresDsn