from fastapi import APIRouter 

router = APIRouter(
    prefix='/admin', tags=['Admin API']
)