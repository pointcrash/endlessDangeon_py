from sqlalchemy.orm import Mapped

from core.models.base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.player_char_rel import PlayerCharacterRelationMixin


class Inventory(IntIdPkMixin, PlayerCharacterRelationMixin, Base):
    _character_id_unique = True
    _character_back_populates = "inventory"

    slots_count: Mapped[int]
    gold: Mapped[int]
