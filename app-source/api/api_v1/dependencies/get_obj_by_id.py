from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud import AsyncCRUDBase
from core.models import db_helper, Base


class GetObjByIDDependence:
    def __init__(self, crud: AsyncCRUDBase):
        self.crud = crud

    async def __call__(
        self,
        obj_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.session_getter),
    ) -> Base:
        obj = await self.crud.get(session=session, obj_id=obj_id)

        if obj is not None:
            return obj

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{self.crud.model.__name__} не найден",
        )
