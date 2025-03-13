import dataclasses
from dataclasses import dataclass
from typing import Any
from uuid import UUID


@dataclass
class ResourceImpl:
    uuid: UUID

    def asdict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

@dataclass
class School(ResourceImpl):
    name: str


@dataclass
class Class(ResourceImpl):
    school_id: UUID
    name: str
