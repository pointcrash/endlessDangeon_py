from core.schemas.enemy import (
    EnemyRead,
    EnemyCreate,
    EnemyUpdate,
    EnemyPartialUpdate,
)
from .base import BaseView

from core.config import settings
from core.models import Enemy
from .crud.enemy import crud


class AsyncView(
    BaseView[
        Enemy,
        EnemyRead,
        EnemyCreate,
        EnemyUpdate,
        EnemyPartialUpdate,
    ]
):
    pass


view = AsyncView(
    model=Enemy,
    crud=crud,
    read_schema=EnemyRead,
    create_schema=EnemyCreate,
    update_schema=EnemyUpdate,
    partial_update_schema=EnemyPartialUpdate,
    prefix=settings.api.v1.enemies,
    tags=["Enemies"],
)

router = view.router
