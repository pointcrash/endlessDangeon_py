from core.schemas.inventory import (
    InventoryRead,
    InventoryCreate,
    InventoryUpdate,
    InventoryPartialUpdate,
)
from .base import BaseView

from core.config import settings
from core.models import Inventory
from .crud.inventory import crud


class AsyncView(
    BaseView[
        Inventory,
        InventoryRead,
        InventoryCreate,
        InventoryUpdate,
        InventoryPartialUpdate,
    ]
):
    pass


view = AsyncView(
    model=Inventory,
    crud=crud,
    read_schema=InventoryRead,
    create_schema=InventoryCreate,
    update_schema=InventoryUpdate,
    partial_update_schema=InventoryPartialUpdate,
    prefix=settings.api.v1.inventory,
    tags=["Inventory"],
)

router = view.router
