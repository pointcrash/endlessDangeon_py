from core.schemas.npc import (
    NPCCreate,
    NPCUpdate,
    NPCPartialUpdate,
)

from api.api_v1.crud import AsyncCRUDBase
from core.models import NPC


class AsyncCRUD(
    AsyncCRUDBase[
        NPC,
        NPCCreate,
        NPCUpdate,
        NPCPartialUpdate,
    ]
):
    pass


crud = AsyncCRUD(NPC)
