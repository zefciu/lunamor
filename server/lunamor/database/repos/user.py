from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from lunamor.database.models.user import User
from lunamor.database.session import get_session


class UserRepository:

    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def is_superuser(self, email: str) -> bool:
        result = await self.session.execute(
                select(User.is_superuser)
                .where(User.email == email)
        )
        return result.scalar_one_or_none() or False

def get_user_repository(session: Annotated[AsyncSession, Depends(get_session)]):
    return UserRepository(session)
