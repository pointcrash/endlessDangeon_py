from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import users as users_crud
from core.config import settings
from core.models import db_helper
from core.schemas.user import UserRead, UserCreate

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await users_crud.get_all_users(session=session)
    return users


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
):
    try:
        user = await users_crud.create_user(session=session, user_create=user_create)
        return user
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Пользователь с такими данными уже существует"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/{telegram_id}", response_model=UserRead)
async def get_users(
    telegram_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    user = await users_crud.get_user_by_telegram_id(
        session=session, telegram_id=telegram_id
    )

    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return user
