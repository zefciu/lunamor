
from fastapi import FastAPI
from pyjwt_key_fetcher import AsyncKeyFetcher
from starlette.requests import Request


class Lunamor(FastAPI):

    jwt_key_fetcher: AsyncKeyFetcher


def get_jwt_fetcher(request: Request) -> AsyncKeyFetcher:
    return request.app.jwt_key_fetcher
