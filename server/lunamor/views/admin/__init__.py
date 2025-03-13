from fastapi import APIRouter

from lunamor.views.admin.school import admin_school_router

admin_router = APIRouter()
admin_router.include_router(admin_school_router, prefix="/school")
