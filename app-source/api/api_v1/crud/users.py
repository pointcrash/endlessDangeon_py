from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas.user import UserCreate


async def get_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_user_by_telegram_id(
    session: AsyncSession, telegram_id: int
) -> User | None:
    stmt = select(User).where(User.telegram_id == telegram_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user


async def create_user(
    user_create: UserCreate,
    session: AsyncSession,
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    try:
        await session.commit()
        # await session.refresh(user)
        return user
    except IntegrityError:
        await session.rollback()
        raise  # Пробрасываем ошибку наверх
