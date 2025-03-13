from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError
from pydantic import BaseModel
from pyjwt_key_fetcher import AsyncKeyFetcher
from pyjwt_key_fetcher.errors import JWTInvalidIssuerError
from starlette.status import HTTP_401_UNAUTHORIZED

from lunamor.app.app import get_jwt_fetcher


http_bearer = HTTPBearer()



async def get_user_id(
    jwt_fetcher: Annotated[AsyncKeyFetcher, Depends(get_jwt_fetcher)],
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)]
) -> str:
    try:
        key = await jwt_fetcher.get_key(credentials.credentials)
    except JWTInvalidIssuerError:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid JWT issuer",
        )
    try:
        decoded = jwt.decode(jwt=credentials.credentials, **key)
    except PyJWTError as err:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Token parsing failed"
        )
    return decoded["email"]
