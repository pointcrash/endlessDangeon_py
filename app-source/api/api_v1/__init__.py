from fastapi import APIRouter

from core.config import settings

from .users import router as users_router
from .characters import router as characters_router

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(users_router)
router.include_router(characters_router)
