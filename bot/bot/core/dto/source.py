from uuid import UUID

from pydantic import BaseModel


class CreateSource(BaseModel):
    user_id: int
    url: str

class Source(CreateSource):
    source_id: UUID