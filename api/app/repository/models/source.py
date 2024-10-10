from uuid import UUID

from sqlalchemy import Uuid, text, BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Source(Base):
    __tablename__ = 'sources'

    source_id: Mapped[UUID] = mapped_column(Uuid,
                                            primary_key=True,
                                            server_default=text('gen_random_uuid()'))
    url: Mapped[str] = mapped_column(String, unique=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.user_id'))

    user: Mapped["User"] = relationship(back_populates='sources')
