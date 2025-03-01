from core.schemas.character import (
    PlayerCharacterCreate,
    PlayerCharacterUpdate,
    PlayerCharacterPartialUpdate,
)


from api.api_v1.crud import AsyncCRUDBase
from core.models import PlayerCharacter


class AsyncCRUDCharacter(
    AsyncCRUDBase[
        PlayerCharacter,
        PlayerCharacterCreate,
        PlayerCharacterUpdate,
        PlayerCharacterPartialUpdate,
    ]
):
    pass


characters_crud = AsyncCRUDCharacter(PlayerCharacter)
