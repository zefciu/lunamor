from typing import Protocol

from lunamor.api.school import SchoolCreationRequest
from lunamor.database.models.school import Class
from lunamor.database.repos.protocol import School


class SchoolService(Protocol):

    async def create_school(self, request: SchoolCreationRequest) -> None: ...
