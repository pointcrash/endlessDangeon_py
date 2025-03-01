from sqlalchemy import Column, Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from core.models import Base

location_association = Table(
    "location_association",
    Base.metadata,
    Column(
        "location_id",
        Integer,
        ForeignKey("locations.id"),
        primary_key=True,
    ),
    Column(
        "related_location_id",
        Integer,
        ForeignKey("locations.id"),
        primary_key=True,
    ),
)
