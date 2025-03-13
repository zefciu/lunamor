from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, \
    async_sessionmaker

from lunamor.database.config import DatabaseConfiguration, get_db_config


def get_engine(config: Annotated[DatabaseConfiguration, Depends(get_db_config)]):
    return create_async_engine(config.DATABASE_URL)


async def get_session(engine: Annotated[AsyncEngine, Depends(get_engine)]):
    async with async_sessionmaker(engine)() as session:
        yield session
        await session.commit()
