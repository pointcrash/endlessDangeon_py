from pydantic import BaseModel


class PlayerCharacterBase(BaseModel):
    name: str


class PlayerCharacterCreate(PlayerCharacterBase):
    pass


class PlayerCharacterRead(PlayerCharacterBase):
    id: int
    lvl: int
    hp: str
    mp: str
    image: str
