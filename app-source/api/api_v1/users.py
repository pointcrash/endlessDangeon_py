from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.users_all_data import UserAllData

from core.config import settings
from core.models import db_helper, User
from core.schemas.user import UserRead, UserCreate, UserUpdate, UserUpdatePartial
from .crud.user_base import users_crud
from .dependencies.users import (
    get_user_by_telegram_id,
    get_user_all_data_by_telegram_id,
)

router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await users_crud.get_all(session=session)
    return users


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    try:
        user = await users_crud.create(session=session, obj_in=user_create)
        return user
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка сервера: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/{telegram_id}", response_model=UserRead)
async def get_user(
    user: User = Depends(get_user_by_telegram_id),
):
    return user


@router.get("/{telegram_id}/all_data", response_model=UserAllData)
async def get_user_all_data(
    user: User = Depends(get_user_all_data_by_telegram_id),
):
    return user


@router.put("/{telegram_id}")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(get_user_by_telegram_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await users_crud.update(
        session=session,
        obj=user,
        obj_in=user_update,
    )


@router.patch("/{telegram_id}")
async def partial_update_user(
    user_update: UserUpdatePartial,
    user: User = Depends(get_user_by_telegram_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await users_crud.update(
        session=session,
        obj=user,
        obj_in=user_update,
        partial=True,
    )


@router.delete("/{telegram_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    obj: User = Depends(get_user_by_telegram_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await users_crud.delete(
        session=session,
        obj=obj,
    )
