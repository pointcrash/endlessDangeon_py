from core.schemas.enemy import (
    EnemyCreate,
    EnemyUpdate,
    EnemyPartialUpdate,
)

from api.api_v1.crud import AsyncCRUDBase
from core.models import Enemy


class AsyncCRUD(
    AsyncCRUDBase[
        Enemy,
        EnemyCreate,
        EnemyUpdate,
        EnemyPartialUpdate,
    ]
):
    pass


crud = AsyncCRUD(Enemy)
