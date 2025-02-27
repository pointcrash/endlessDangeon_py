from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Inventory
from core.schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryPartialUpdate,
)


async def get_all_inventory(
    session: AsyncSession,
) -> Sequence[Inventory]:
    stmt = select(Inventory).order_by(Inventory.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_inventory_by_id(
    session: AsyncSession, inventory_id: int
) -> Inventory | None:
    stmt = select(Inventory).where(Inventory.id == inventory_id)
    # result = await session.execute(stmt)
    # inventory = result.scalar_one_or_none()
    inventory: Inventory | None = await session.scalar(stmt)
    return inventory


async def create_inventory(
    inventory_create: InventoryCreate,
    session: AsyncSession,
) -> Inventory:
    inventory = Inventory(**inventory_create.model_dump())
    session.add(inventory)
    try:
        await session.commit()
        return inventory
    except IntegrityError:
        await session.rollback()
        raise


async def update_inventory(
    session: AsyncSession,
    inventory: Inventory,
    inventory_update: InventoryUpdate | InventoryPartialUpdate,
    partial: bool = False,
) -> Inventory:
    for name, value in inventory_update.model_dump(exclude_unset=partial).items():
        setattr(inventory, name, value)
    await session.commit()
    return inventory


async def delete_inventory(
    session: AsyncSession,
    inventory: Inventory,
) -> None:
    await session.delete(inventory)
    await session.commit()
