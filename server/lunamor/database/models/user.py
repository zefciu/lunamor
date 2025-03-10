from uuid import UUID

from sqlalchemy import Uuid, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from lunamor.database.models.base import Base


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True)
    email: Mapped[str] = mapped_column(Text(), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(Text(), nullable=False)
    last_name: Mapped[str] = mapped_column(Text(), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean())


class Child(Base):
    __tablename__ = "children"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True)
    parent_id: Mapped[UUID] = mapped_column(ForeignKey("users.uuid"))
    class_id: Mapped[UUID] = mapped_column(ForeignKey("classes.uuid"))
    first_name: Mapped[str] = mapped_column(Text(), nullable=False)
    last_name: Mapped[str] = mapped_column(Text(), nullable=False)
