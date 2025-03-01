from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar, Generic, Optional
from pydantic import BaseModel

from api.api_v1.crud import AsyncCRUDBase
from api.api_v1.dependencies.get_obj_by_id import GetObjByIDDepend
from core.models import db_helper, Base

ModelType = TypeVar("ModelType", bound=Base)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
PartialUpdateSchemaType = TypeVar("PartialUpdateSchemaType", bound=BaseModel)


class BaseView(
    Generic[
        ModelType,
        ReadSchemaType,
        CreateSchemaType,
        UpdateSchemaType,
        PartialUpdateSchemaType,
    ]
):
    def __init__(
        self,
        model: Type[ModelType],
        crud: AsyncCRUDBase,
        read_schema: Type[ReadSchemaType],
        create_schema: Type[CreateSchemaType],
        update_schema: Type[UpdateSchemaType],
        partial_update_schema: Type[PartialUpdateSchemaType],
        prefix: str,
        tags: Optional[list[str]] = None,
    ):
        self.router = APIRouter(prefix=prefix, tags=tags or [])
        self.crud = crud
        self.model = model
        # self.read_schema = read_schema
        # self.create_schema = create_schema
        # self.update_schema = update_schema
        # self.partial_update_schema = partial_update_schema
        self.get_obj_by_id = GetObjByIDDepend(self.crud)

        @self.router.get("", response_model=list[read_schema])
        async def get_all(session: AsyncSession = Depends(db_helper.session_getter)):
            return await self.crud.get_all(session)

        @self.router.get("/{obj_id}", response_model=read_schema)
        async def get_one(
            obj: ModelType = Depends(self.get_obj_by_id),
        ):
            return obj

        @self.router.post(
            "", response_model=read_schema, status_code=status.HTTP_201_CREATED
        )
        async def create(
            obj_in: create_schema,
            session: AsyncSession = Depends(db_helper.session_getter),
        ):
            return await self.crud.create(session, obj_in)

        @self.router.put("/{obj_id}", response_model=read_schema)
        async def update(
            obj_in: update_schema,
            obj: ModelType = Depends(self.get_obj_by_id),
            session: AsyncSession = Depends(db_helper.session_getter),
        ):
            return await self.crud.update(session, obj, obj_in)

        @self.router.patch("/{obj_id}", response_model=read_schema)
        async def partial_update(
            obj_in: partial_update_schema,
            obj: ModelType = Depends(self.get_obj_by_id),
            session: AsyncSession = Depends(db_helper.session_getter),
        ):
            return await self.crud.update(session, obj, obj_in, partial=True)

        @self.router.delete("/{obj_id}", status_code=status.HTTP_204_NO_CONTENT)
        async def delete(
            obj: ModelType = Depends(self.get_obj_by_id),
            session: AsyncSession = Depends(db_helper.session_getter),
        ):
            await self.crud.delete(session, obj)
