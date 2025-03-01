from core.schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryPartialUpdate,
)

from api.api_v1.crud import AsyncCRUDBase
from core.models import Inventory


class AsyncCRUD(
    AsyncCRUDBase[
        Inventory,
        InventoryCreate,
        InventoryUpdate,
        InventoryPartialUpdate,
    ]
):
    pass


crud = AsyncCRUD(Inventory)
