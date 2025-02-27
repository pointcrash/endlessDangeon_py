from pydantic import BaseModel


class InventoryBase(BaseModel):
    pass


class InventoryExpandBase(InventoryBase):
    slots_count: int
    gold: int


class InventoryCreate(InventoryBase):
    character_id: int


class InventoryUpdate(InventoryExpandBase):
    pass


class InventoryPartialUpdate(InventoryExpandBase):
    slots_count: int | None = None
    gold: int | None = None


class InventoryRead(InventoryExpandBase):
    character_id: int
    id: int
