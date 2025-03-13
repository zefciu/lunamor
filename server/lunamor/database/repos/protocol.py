from typing import Mapping, Any, Iterable
from uuid import UUID

from asyncpg.protocol.protocol import Protocol

class Resource(Protocol):
    uuid: UUID

    def asdict(self) -> Mapping[str, Any]: ...


class School(Resource):
    name: str


class Class(Resource):
    school_uuid: UUID
    name: str


class SchoolRepository(Protocol):
    async def insert_school(self, school: School) -> None: ...


    async def insert_classes(self, classes: Iterable[Class]) -> None: ...


class UserRepository(Protocol):

    async def is_superuser(self, email: str) -> bool: ...
