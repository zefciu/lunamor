from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from lunamor.app.wiring.repository import get_school_repository
from lunamor.business.school import SchoolServiceImpl
from lunamor.database.repos.protocol import SchoolRepository


def get_school_service(repo: Annotated[SchoolRepository, Depends(get_school_repository)]):
    return SchoolServiceImpl(repo)
