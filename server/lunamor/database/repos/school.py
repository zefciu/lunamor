from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from lunamor.database.repos.protocol import School, Class
from lunamor.database.models.school import School as DBSchool, Class as DBClass


class SQLSchoolRepository:

    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_school(self, school: School) -> None:
        self.session.add(DBSchool(**school.asdict()))
        await self.session.flush()

    async def insert_classes(self, classes: Iterable[Class]) -> None:
        self.session.add_all(DBClass(**class_.asdict()) for class_ in classes)
        await self.session.flush()
