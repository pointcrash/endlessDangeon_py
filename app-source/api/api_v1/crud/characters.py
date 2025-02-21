from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import PlayerCharacter
from core.schemas.character import (
    PlayerCharacterCreate,
    PlayerCharacterUpdate,
    PlayerCharacterPartialUpdate,
)


async def get_all_characters(
    session: AsyncSession,
) -> Sequence[PlayerCharacter]:
    stmt = select(PlayerCharacter).order_by(PlayerCharacter.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_character_by_id(
    session: AsyncSession, character_id: int
) -> PlayerCharacter | None:
    stmt = select(PlayerCharacter).where(PlayerCharacter.id == character_id)
    result = await session.execute(stmt)
    character = result.scalar_one_or_none()
    return character


async def create_character(
    character_create: PlayerCharacterCreate,
    session: AsyncSession,
) -> PlayerCharacter:
    character = PlayerCharacter(**character_create.model_dump())
    session.add(character)
    try:
        await session.commit()
        return character
    except IntegrityError:
        await session.rollback()
        raise


async def update_character(
    session: AsyncSession,
    character: PlayerCharacter,
    character_update: PlayerCharacterUpdate | PlayerCharacterPartialUpdate,
    partial: bool = False,
) -> PlayerCharacter:
    for name, value in character_update.model_dump(exclude_unset=partial).items():
        setattr(character, name, value)
    await session.commit()
    return character


async def delete_character(
    session: AsyncSession,
    character: PlayerCharacter,
) -> None:
    await session.delete(character)
    await session.commit()
