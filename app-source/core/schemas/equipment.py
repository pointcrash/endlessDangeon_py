from pydantic import BaseModel


class EquipmentBase(BaseModel):
    pass


class EquipmentExpandBase(EquipmentBase):
    helmet: int | None = None
    body_armour: int | None = None
    boots: int | None = None
    gloves: int | None = None
    backpack: int | None = None
    weapon_1: int | None = None
    weapon_2: int | None = None


class EquipmentCreate(EquipmentBase):
    character_id: int


class EquipmentUpdate(EquipmentExpandBase):
    pass


class EquipmentPartialUpdate(EquipmentExpandBase):
    helmet: int | None = None
    body_armour: int | None = None
    boots: int | None = None
    gloves: int | None = None
    backpack: int | None = None
    weapon_1: int | None = None
    weapon_2: int | None = None


class EquipmentRead(EquipmentExpandBase):
    character_id: int
    id: int
