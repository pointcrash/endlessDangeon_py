from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.character import (
    PlayerCharacterRead,
    PlayerCharacterCreate,
    PlayerCharacterUpdate,
    PlayerCharacterPartialUpdate,
)
from .crud import characters as characters_crud
from core.config import settings
from core.models import db_helper, PlayerCharacter
from .dependencies.characters import get_character_by_id

router = APIRouter(prefix=settings.api.v1.characters, tags=["PlayerCharacters"])


@router.get("", response_model=list[PlayerCharacterRead])
async def get_characters(session: AsyncSession = Depends(db_helper.session_getter)):
    characters = await characters_crud.get_all_characters(session=session)
    return characters


@router.post(
    "", response_model=PlayerCharacterRead, status_code=status.HTTP_201_CREATED
)
async def create_character(
    character_create: PlayerCharacterCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    try:
        character = await characters_crud.create_character(
            session=session, character_create=character_create
        )
        return character

    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Персонаж с такими данными уже существует"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/{character_id}", response_model=PlayerCharacterRead)
async def get_character(
    character: PlayerCharacter = Depends(get_character_by_id),
):
    return character


@router.put("/{character_id}")
async def update_character(
    character_update: PlayerCharacterUpdate,
    character: PlayerCharacter = Depends(get_character_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await characters_crud.update_character(
        session=session,
        character=character,
        character_update=character_update,
    )


@router.patch("/{character_id}")
async def partial_update_character(
    character_update: PlayerCharacterPartialUpdate,
    character: PlayerCharacter = Depends(get_character_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await characters_crud.update_character(
        session=session,
        character=character,
        character_update=character_update,
        partial=True,
    )


@router.delete("/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_character(
    character: PlayerCharacter = Depends(get_character_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await characters_crud.delete_character(
        session=session,
        character=character,
    )
