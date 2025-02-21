from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models.player_char import PlayerCharacter


class PlayerCharacterRelationMixin:
    _character_id_nullable: bool = False
    _character_id_unique: bool = False
    _character_back_populates: str | None = None

    @declared_attr
    def character_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("player_character.id"),
            unique=cls._character_id_unique,
            nullable=cls._character_id_nullable,
        )

    @declared_attr
    def character(cls) -> Mapped["PlayerCharacter"]:
        return relationship(
            "PlayerCharacter",
            back_populates=cls._character_back_populates,
        )
