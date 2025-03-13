from pydantic import BaseModel


class SchoolCreationRequest(BaseModel):
    name: str
    class_names: list[str]
