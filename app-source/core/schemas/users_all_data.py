from .character import PlayerCharacterExpandBase
from .equipment import EquipmentRead
from .inventorys import InventoryRead
from .user import UserBase


class PlayerCharacterAllData(PlayerCharacterExpandBase):
    id: int
    equipment: EquipmentRead | None
    inventory: InventoryRead | None


class UserAllData(UserBase):
    id: int
    telegram_id: int
    character: PlayerCharacterAllData
