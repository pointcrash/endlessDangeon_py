from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from .associations import location_association

if TYPE_CHECKING:
    from .player_char import PlayerCharacter
    from .npc import NPC
    from .enemy import Enemy


class Location(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    bg: Mapped[str] = mapped_column(nullable=True)

    characters: Mapped[list["PlayerCharacter"]] = relationship(
        back_populates="location"
    )
    npcs: Mapped[list["NPC"]] = relationship(back_populates="location")
    enemies: Mapped[list["Enemy"]] = relationship(back_populates="location")

    related_locations: Mapped[list[Location]] = relationship(
        "Location",
        secondary=location_association,
        primaryjoin="Location.id == location_association.c.location_id",
        secondaryjoin="Location.id == location_association.c.related_location_id",
        backref="related_to",
    )
