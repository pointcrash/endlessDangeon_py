from typing import Type, TypeVar, Generic, Sequence

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from core.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
PartialUpdateSchemaType = TypeVar("PartialUpdateSchemaType", bound=BaseModel)


class AsyncCRUDBase(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType, PartialUpdateSchemaType]
):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, session: AsyncSession, obj_id: int) -> ModelType:
        stmt = select(self.model).where(self.model.id == obj_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> Sequence[ModelType]:
        stmt = select(self.model)
        result = await session.scalars(stmt)
        return result.all()

    async def create(
        self,
        session: AsyncSession,
        obj_in: CreateSchemaType,
    ) -> ModelType:
        obj = self.model(**obj_in.model_dump())
        session.add(obj)
        try:
            await session.commit()
            return obj
        except IntegrityError:
            await session.rollback()
            raise

    async def update(
        self,
        session: AsyncSession,
        obj: ModelType,
        obj_in: UpdateSchemaType | PartialUpdateSchemaType,
        partial: bool = False,
    ) -> ModelType:
        for key, value in obj_in.model_dump(exclude_unset=partial).items():
            setattr(obj, key, value)
        await session.commit()
        return obj

    async def delete(self, session: AsyncSession, obj: ModelType) -> None:
        await session.delete(obj)
        await session.commit()
