from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .abs.character import Character
from .mixins.user_relation import UserRelationMixin


if TYPE_CHECKING:
    from .char_equip import CharacterEquipment
    from .inventory import Inventory


class PlayerCharacter(Character, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "character"
    _location_back_populates = "characters"

    equipment: Mapped["CharacterEquipment"] = relationship(back_populates="character")
    inventory: Mapped["Inventory"] = relationship(back_populates="character")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        from . import CharacterEquipment
        from . import Inventory

        self.equipment = CharacterEquipment(character=self)
        self.inventory = Inventory(character=self)
