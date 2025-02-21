from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Item(IntIdPkMixin, Base):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    type: Mapped[str]
    cost: Mapped[int] = mapped_column(default=1, server_default="1")
    image: Mapped[str]
