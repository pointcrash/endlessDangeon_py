from pydantic import BaseModel


class PlayerCharacterBase(BaseModel):
    name: str
    user_id: int


class PlayerCharacterExpandBase(BaseModel):
    lvl: int
    hp: int
    mp: int
    image: str


class PlayerCharacterCreate(PlayerCharacterBase):
    pass


class PlayerCharacterUpdate(PlayerCharacterExpandBase):
    pass


class PlayerCharacterPartialUpdate(PlayerCharacterExpandBase):
    name: str | None = None
    lvl: int | None = None
    hp: int | None = None
    mp: int | None = None
    image: str | None = None


class PlayerCharacterRead(PlayerCharacterExpandBase):
    id: int
