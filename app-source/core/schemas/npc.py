from pydantic import BaseModel


class NPCBase(BaseModel):
    name: str
    lvl: int
    hp: int
    mp: int
    image: str | None
    location_id: int | None


class NPCExpandBase(NPCBase):
    pass


class NPCCreate(NPCExpandBase):
    pass


class NPCUpdate(NPCExpandBase):
    pass


class NPCPartialUpdate(NPCExpandBase):
    name: str | None = None
    lvl: int | None = None
    hp: int | None = None
    mp: int | None = None
    image: str | None = None
    location_id: int | None = None


class NPCRead(NPCExpandBase):
    id: int
