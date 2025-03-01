from pydantic import BaseModel

from core.schemas.character import PlayerCharacterBase
from core.schemas.enemy import EnemyRead
from core.schemas.npc import NPCRead


class LocationBase(BaseModel):
    name: str
    bg: str | None


class LocationExpandBase(LocationBase):
    pass


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationExpandBase):
    pass


class LocationPartialUpdate(LocationExpandBase):
    name: str | None = None
    bg: str | None = None


class LocationRead(LocationExpandBase):
    id: int
    characters: list[PlayerCharacterBase] | None
    npcs: list[NPCRead] | None
    enemies: list[EnemyRead] | None
    related_locations: list[LocationBase] | None
