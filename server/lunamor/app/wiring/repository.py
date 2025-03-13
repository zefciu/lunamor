from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from lunamor.database.repos.school import SQLSchoolRepository
from lunamor.database.session import get_session


def get_school_repository(session: Annotated[AsyncSession, Depends(get_session)]):
    return SQLSchoolRepository(session)
