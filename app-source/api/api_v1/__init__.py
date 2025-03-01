from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from .character_base import router as characters_router
from .inventory_base import router as inventory_router
from .location import router as location_router


router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(users_router)
router.include_router(characters_router)
router.include_router(inventory_router)
router.include_router(location_router)
