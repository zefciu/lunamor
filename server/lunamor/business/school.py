from typing import Annotated
from uuid import uuid4

from lunamor.api.school import SchoolCreationRequest
from lunamor.database.repos.protocol import SchoolRepository
from lunamor.data.school import School, Class


class SchoolServiceImpl:
    repository: SchoolRepository

    def __init__(self, repository: SchoolRepository):
        self.repository = repository

    async def create_school(self, request: SchoolCreationRequest) -> None:
        school_uuid = uuid4()
        await self.repository.insert_school(
            School(
                uuid=school_uuid,
                name=request.name,
            )
        )
        await self.repository.insert_classes(
            Class(
                uuid=uuid4(),
                school_id=school_uuid,
                name=name
            ) for name in request.class_names
        )
