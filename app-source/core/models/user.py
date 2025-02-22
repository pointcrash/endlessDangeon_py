from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


if TYPE_CHECKING:
    from .player_char import PlayerCharacter


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    language: Mapped[str] = mapped_column()

    character: Mapped["PlayerCharacter"] = relationship(back_populates="user")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        from .player_char import PlayerCharacter

        self.character = PlayerCharacter(user=self)
