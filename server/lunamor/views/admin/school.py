from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED

from lunamor.api.school import SchoolCreationRequest
from lunamor.app.wiring.business import get_school_service
from lunamor.auth.checkers import superuser
from lunamor.business.protocol import SchoolService

admin_school_router = APIRouter()


@admin_school_router.post("/")
async def create_school(
    school: SchoolCreationRequest,
    school_service: Annotated[SchoolService, Depends(get_school_service)],
    _ = Depends(superuser),
) -> Response:
    await school_service.create_school(school)
    return Response(status_code=HTTP_201_CREATED)
