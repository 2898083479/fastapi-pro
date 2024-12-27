from fastapi import APIRouter

from .test1 import router as test1_router

router = APIRouter(
    prefix='', tags=['index API']
)


router.include_router(test1_router)
