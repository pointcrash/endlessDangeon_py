from pydantic import BaseModel


class EnemyBase(BaseModel):
    name: str
    lvl: int
    hp: int
    mp: int
    image: str | None
    location_id: int | None


class EnemyExpandBase(EnemyBase):
    pass


class EnemyCreate(EnemyExpandBase):
    pass


class EnemyUpdate(EnemyExpandBase):
    pass


class EnemyPartialUpdate(EnemyExpandBase):
    name: str | None = None
    lvl: int | None = None
    hp: int | None = None
    mp: int | None = None
    image: str | None = None
    location_id: int | None = None


class EnemyRead(EnemyExpandBase):
    id: int
