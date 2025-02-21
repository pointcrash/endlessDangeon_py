from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .abs.character import Character
from .mixins.user_relation import UserRelationMixin


if TYPE_CHECKING:
    from . import CharacterEquipment


class PlayerCharacter(Character, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "character"

    equipment: Mapped["CharacterEquipment"] = relationship(back_populates="character")
