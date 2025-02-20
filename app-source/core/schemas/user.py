from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    telegram_id: int
    language: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
