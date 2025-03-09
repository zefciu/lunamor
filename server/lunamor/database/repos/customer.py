from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from lunamor.database.models.customer import Customer


class CustomerExists(BaseException):
    pass


async def register_customer(session: AsyncSession, customer: Customer):
    session.add(customer)
    try:
        await session.flush()
    except IntegrityError:
        raise CustomerExists()
