from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from .mixins.int_id_pk import IntIdPkMixin
from .mixins.player_char_rel import PlayerCharacterRelationMixin


class Inventory(IntIdPkMixin, PlayerCharacterRelationMixin, Base):
    _character_id_unique = True
    _character_back_populates = "inventory"

    slots_count: Mapped[int] = mapped_column(default=10, server_default="10")
    gold: Mapped[int] = mapped_column(default=100, server_default="100")
