from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models.location import Location


class LocationRelationMixin:
    _location_id_nullable: bool = False
    _location_id_unique: bool = False
    _location_back_populates: str | None = None

    @declared_attr
    def location_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("locations.id"),
            unique=cls._location_id_unique,
            nullable=cls._location_id_nullable,
        )

    @declared_attr
    def location(cls) -> Mapped["Location"]:
        return relationship(
            "Location",
            back_populates=cls._location_back_populates,
        )
