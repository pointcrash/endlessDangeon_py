from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    language: str


class UserCreate(UserBase):
    telegram_id: int


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(UserBase):
    username: str | None = None
    language: str | None = None


class UserRead(UserBase):
    id: int
    telegram_id: int
