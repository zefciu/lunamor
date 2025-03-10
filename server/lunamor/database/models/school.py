from uuid import UUID

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from lunamor.database.models.base import Base


class School(Base):
    __tablename__ = "schools"

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text())


class Class(Base):
    __tablename__ = "classes"

    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    school_id: Mapped[UUID] = mapped_column(ForeignKey("schools.uuid"))
