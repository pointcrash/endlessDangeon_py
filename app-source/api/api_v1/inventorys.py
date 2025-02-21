from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.inventorys import (
    InventoryRead,
    InventoryCreate,
    InventoryUpdate,
    InventoryPartialUpdate,
)
from .crud import inventorys as inventory_crud
from core.config import settings
from core.models import db_helper, Inventory
from .dependencies.inventorys import get_inventory_by_id


router = APIRouter(prefix=settings.api.v1.inventory, tags=["Inventory"])


@router.get("", response_model=list[InventoryRead])
async def get_inventory(session: AsyncSession = Depends(db_helper.session_getter)):
    inventory = await inventory_crud.get_all_inventory(session=session)
    return inventory


@router.post("", response_model=InventoryRead, status_code=status.HTTP_201_CREATED)
async def create_inventory(
    inventory_create: InventoryCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    try:
        inventory = await inventory_crud.create_inventory(
            session=session, inventory_create=inventory_create
        )
        return inventory

    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Инвентарь с такими данными уже существует"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/{inventory_id}", response_model=InventoryRead)
async def get_inventory(
    inventory: Inventory = Depends(get_inventory_by_id),
):
    return inventory


@router.put("/{inventory_id}")
async def update_inventory(
    inventory_update: InventoryUpdate,
    inventory: Inventory = Depends(get_inventory_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await inventory_crud.update_inventory(
        session=session,
        inventory=inventory,
        inventory_update=inventory_update,
    )


@router.patch("/{inventory_id}")
async def partial_update_inventory(
    inventory_update: InventoryPartialUpdate,
    inventory: Inventory = Depends(get_inventory_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await inventory_crud.update_inventory(
        session=session,
        inventory=inventory,
        inventory_update=inventory_update,
        partial=True,
    )


@router.delete("/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory(
    inventory: Inventory = Depends(get_inventory_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
) -> None:
    await inventory_crud.delete_inventory(
        session=session,
        inventory=inventory,
    )
