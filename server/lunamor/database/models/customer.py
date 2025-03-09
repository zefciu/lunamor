from uuid import UUID

from sqlalchemy import Uuid, Text
from sqlalchemy.orm import Mapped, mapped_column

from lunamor.database.models.base import Base


class Customer(Base):
    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True)
    email: Mapped[str] = mapped_column(Text(), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(Text(), nullable=False)
    last_name: Mapped[str] = mapped_column(Text(), nullable=False)
