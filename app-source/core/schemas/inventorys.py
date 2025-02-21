from pydantic import BaseModel


class InventoryBase(BaseModel):
    user_id: int


class InventoryExpandBase(InventoryBase):
    slots_count: int
    gold: int


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryExpandBase):
    pass


class InventoryPartialUpdate(InventoryExpandBase):
    slots_count: int | None = None
    gold: int | None = None


class InventoryRead(InventoryExpandBase):
    id: int
