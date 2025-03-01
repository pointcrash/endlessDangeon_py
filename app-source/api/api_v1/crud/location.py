from core.schemas.location import (
    LocationCreate,
    LocationUpdate,
    LocationPartialUpdate,
)

from api.api_v1.crud import AsyncCRUDBase
from core.models import Location


class AsyncCRUD(
    AsyncCRUDBase[
        Location,
        LocationCreate,
        LocationUpdate,
        LocationPartialUpdate,
    ]
):
    pass


crud = AsyncCRUD(Location)
