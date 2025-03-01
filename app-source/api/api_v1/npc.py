from core.schemas.npc import (
    NPCRead,
    NPCCreate,
    NPCUpdate,
    NPCPartialUpdate,
)
from .base import BaseView

from core.config import settings
from core.models import NPC
from .crud.npc import crud


class AsyncView(
    BaseView[
        NPC,
        NPCRead,
        NPCCreate,
        NPCUpdate,
        NPCPartialUpdate,
    ]
):
    pass


view = AsyncView(
    model=NPC,
    crud=crud,
    read_schema=NPCRead,
    create_schema=NPCCreate,
    update_schema=NPCUpdate,
    partial_update_schema=NPCPartialUpdate,
    prefix=settings.api.v1.npc,
    tags=["NPC"],
)

router = view.router
