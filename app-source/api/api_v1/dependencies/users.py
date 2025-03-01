from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.user_base import users_crud
from core.models import db_helper, User


async def get_user_by_telegram_id(
    telegram_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> User:
    user = await users_crud.get(session=session, telegram_id=telegram_id)

    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
    )


async def get_user_all_data_by_telegram_id(
    telegram_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> User:
    user = await users_crud.get_all_user_data_by_telegram_id(
        session=session, telegram_id=telegram_id
    )

    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
    )
