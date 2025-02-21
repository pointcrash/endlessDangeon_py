from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    telegram_id: int
    language: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(UserBase):
    username: str | None = None
    telegram_id: int | None = None
    language: str | None = None


class UserRead(UserBase):
    id: int
