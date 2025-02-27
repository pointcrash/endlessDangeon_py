from .character import PlayerCharacterExpandBase
from .equipment import EquipmentRead
from .inventory import InventoryRead
from .location import LocationRead
from .user import UserBase


class PlayerCharacterAllData(PlayerCharacterExpandBase):
    id: int
    equipment: EquipmentRead | None
    inventory: InventoryRead | None
    location: LocationRead | None


class UserAllData(UserBase):
    id: int
    telegram_id: int
    character: PlayerCharacterAllData
