from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models import User, PlayerCharacter
from core.schemas.user import UserCreate, UserUpdate, UserUpdatePartial


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


async def get_all_user_data_by_telegram_id(
    session: AsyncSession, telegram_id: int
) -> User | None:
    stmt = (
        select(User)
        .where(User.telegram_id == telegram_id)
        .options(
            joinedload(User.character),
            joinedload(User.character).joinedload(PlayerCharacter.inventory),
            joinedload(User.character).joinedload(PlayerCharacter.equipment),
        )
    )
    user = await session.scalar(stmt)
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
        raise


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate | UserUpdatePartial,
    partial: bool = False,
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:
    await session.delete(user)
    await session.commit()
