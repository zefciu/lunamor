from contextlib import asynccontextmanager

from pyjwt_key_fetcher import AsyncKeyFetcher

from lunamor.app.app import Lunamor
from lunamor.views.admin import admin_router


@asynccontextmanager
async def lifespan(app: Lunamor):
    app.jwt_key_fetcher = AsyncKeyFetcher()
    yield


app = Lunamor(lifespan=lifespan)
app.include_router(admin_router, prefix="/admin")
