from core.schemas.character import (
    PlayerCharacterRead,
    PlayerCharacterCreate,
    PlayerCharacterUpdate,
    PlayerCharacterPartialUpdate,
)
from .base import BaseView

from core.config import settings
from core.models import PlayerCharacter
from .crud.characters import characters_crud


class AsyncViewCharacter(
    BaseView[
        PlayerCharacter,
        PlayerCharacterRead,
        PlayerCharacterCreate,
        PlayerCharacterUpdate,
        PlayerCharacterPartialUpdate,
    ]
):
    pass


character_view = AsyncViewCharacter(
    model=PlayerCharacter,
    crud=characters_crud,
    read_schema=PlayerCharacterRead,
    create_schema=PlayerCharacterCreate,
    update_schema=PlayerCharacterUpdate,
    partial_update_schema=PlayerCharacterPartialUpdate,
    prefix=settings.api.v1.characters,
    tags=["PlayerCharacters"],
)

router = character_view.router
