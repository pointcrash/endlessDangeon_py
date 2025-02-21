from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, PlayerCharacter
from api.api_v1.crud import characters as character_crud


async def get_character_by_id(
    character_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> PlayerCharacter:
    character = await character_crud.get_character_by_id(
        session=session, character_id=character_id
    )

    if character is not None:
        return character

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Персонаж не найден"
    )
