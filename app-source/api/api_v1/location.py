from core.schemas.location import (
    LocationRead,
    LocationCreate,
    LocationUpdate,
    LocationPartialUpdate,
)
from .base import BaseView

from core.config import settings
from core.models import Location
from .crud.location import crud


class AsyncView(
    BaseView[
        Location,
        LocationRead,
        LocationCreate,
        LocationUpdate,
        LocationPartialUpdate,
    ]
):
    pass


view = AsyncView(
    model=Location,
    crud=crud,
    read_schema=LocationRead,
    create_schema=LocationCreate,
    update_schema=LocationUpdate,
    partial_update_schema=LocationPartialUpdate,
    prefix=settings.api.v1.locations,
    tags=["Locations"],
)

router = view.router
