from sqlalchemy.orm import Mapped

from core.models.base import Base
from .mixins.player_char_rel import PlayerCharacterRelationMixin


class CharacterEquipment(PlayerCharacterRelationMixin, Base):
    _character_id_unique = True
    _character_back_populates = "equipment"

    helmet: Mapped[int]
    body_armour: Mapped[int]
    boots: Mapped[int]
    gloves: Mapped[int]
    backpack: Mapped[int]
    weapon_1: Mapped[int]
    weapon_2: Mapped[int]
