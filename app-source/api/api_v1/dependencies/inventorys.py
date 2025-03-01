# from typing import Annotated
#
# from fastapi import Path, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.models import db_helper, Inventory
# from api.api_v1.crud import inventorys as inventory_crud
#
#
# async def get_inventory_by_id(
#     inventory_id: Annotated[int, Path],
#     session: AsyncSession = Depends(db_helper.session_getter),
# ) -> Inventory:
#     inventory = await inventory_crud.get_inventory_by_id(
#         session=session, inventory_id=inventory_id
#     )
#
#     if inventory is not None:
#         return inventory
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail="Персонаж не найден"
#     )
