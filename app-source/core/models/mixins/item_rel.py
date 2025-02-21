from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models.item import Item


class ItemRelationMixin:
    _item_id_nullable: bool = False
    _item_id_unique: bool = False
    _item_back_populates: str | None = None

    @declared_attr
    def item_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("items.id"),
            unique=cls._item_id_unique,
            nullable=cls._item_id_nullable,
        )

    @declared_attr
    def item(cls) -> Mapped["Item"]:
        return relationship(
            "Item",
            back_populates=cls._item_back_populates,
        )
