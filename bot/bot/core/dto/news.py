from datetime import datetime

from pydantic import BaseModel


class NewsItem(BaseModel):
    title: str
    link: str
    description: str | None = None
    category: str | None = None
    pub_date: datetime