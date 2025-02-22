from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.player_char_rel import PlayerCharacterRelationMixin


class CharacterEquipment(IntIdPkMixin, PlayerCharacterRelationMixin, Base):
    _character_id_unique = True
    _character_back_populates = "equipment"

    helmet: Mapped[int] = mapped_column(nullable=True)
    body_armour: Mapped[int] = mapped_column(nullable=True)
    boots: Mapped[int] = mapped_column(nullable=True)
    gloves: Mapped[int] = mapped_column(nullable=True)
    backpack: Mapped[int] = mapped_column(nullable=True)
    weapon_1: Mapped[int] = mapped_column(nullable=True)
    weapon_2: Mapped[int] = mapped_column(nullable=True)
