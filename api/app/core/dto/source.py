from uuid import UUID

from pydantic import BaseModel, HttpUrl


class CreateSource(BaseModel):
    user_id: int
    url: str

class Source(CreateSource):
    source_id: UUID