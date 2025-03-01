from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from api.api_v1.crud import AsyncCRUDBase
from core.models import User, PlayerCharacter, Location
from core.schemas.user import UserCreate, UserUpdate, UserUpdatePartial


class AsyncCRUDUser(AsyncCRUDBase[User, UserCreate, UserUpdate, UserUpdatePartial]):
    async def get(self, session: AsyncSession, telegram_id: int) -> User:
        stmt = select(self.model).where(self.model.telegram_id == telegram_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all_user_data_by_telegram_id(
        self,
        session: AsyncSession,
        telegram_id: int,
    ) -> User | None:
        stmt = (
            select(self.model)
            .where(self.model.telegram_id == telegram_id)
            .options(
                joinedload(User.character),
                joinedload(User.character).joinedload(PlayerCharacter.inventory),
                joinedload(User.character).joinedload(PlayerCharacter.equipment),
                joinedload(User.character).joinedload(PlayerCharacter.location),
                joinedload(User.character)
                .joinedload(PlayerCharacter.location)
                .joinedload(Location.npcs),
                joinedload(User.character)
                .joinedload(PlayerCharacter.location)
                .joinedload(Location.enemies),
                joinedload(User.character)
                .joinedload(PlayerCharacter.location)
                .joinedload(Location.characters),
                joinedload(User.character)
                .joinedload(PlayerCharacter.location)
                .joinedload(Location.related_locations),
            )
        )
        return await session.scalar(stmt)


users_crud = AsyncCRUDUser(User)
