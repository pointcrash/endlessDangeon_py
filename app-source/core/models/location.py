from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


if TYPE_CHECKING:
    from .player_char import PlayerCharacter
    from .npc import NPC


class Location(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    bg: Mapped[str] = mapped_column(nullable=True)

    characters: Mapped["PlayerCharacter"] = relationship(back_populates="location")
    npcs: Mapped["NPC"] = relationship(back_populates="location")
