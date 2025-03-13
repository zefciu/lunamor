from typing import Annotated

from fastapi import Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from lunamor.auth.models import get_user_id
from lunamor.database.repos.protocol import UserRepository
from lunamor.database.repos.user import get_user_repository


async def superuser(
    user_id: Annotated[str, Depends(get_user_id)],
    user_repository: Annotated[UserRepository, Depends(get_user_repository)]
) -> None:
    if not (await user_repository.is_superuser(user_id)):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
