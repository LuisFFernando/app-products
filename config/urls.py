from fastapi import APIRouter
from app.api.views import meta_views
from app.api.views import user_views
from app.api.views import product_views


urls = APIRouter()

urls.include_router(
    meta_views.router,
    prefix=""
)


urls.include_router(
    user_views.router,
    prefix="/api/v1"
)
urls.include_router(
    product_views.router,
    prefix="/api/v1"
)
