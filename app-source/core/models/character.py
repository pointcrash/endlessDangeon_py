from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Character(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    lvl: Mapped[int] = mapped_column(default=1, server_default="1")
    hp: Mapped[int] = mapped_column(default=1, server_default="1")
    mp: Mapped[int] = mapped_column(default=0, server_default="0")
