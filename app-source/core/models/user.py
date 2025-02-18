from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    language: Mapped[str] = mapped_column()
