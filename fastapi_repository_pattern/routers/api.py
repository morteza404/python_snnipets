from fastapi import APIRouter
from routers.v1 import region, city

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(region.router)
router.include_router(city.router)