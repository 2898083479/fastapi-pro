from fastapi import FastAPI, Query, Path, Body, Cookie, Header, APIRouter
from typing import Annotated, List, Literal, Any
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from datetime import datetime, time, date, timedelta

router = APIRouter(
    prefix='/test3', tags=['test3 API']
)

class Cookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str = Field(..., description='The session ID of the user'),
    fatebook_tracker: str | None = None,
    googall_tracker: str | None = None
    
class Headers(BaseModel):
    host: str
    save_data: bool
    x_tag: list[str]
    text_type: Literal['docx', 'pdf']
    
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    
    
@router.get('/test01/')
async def test01(
    cookies: Annotated[Cookies, Cookie()]
):
    return {"cookies": cookies}

@router.get('/test02/')
async def test02(
    headers: Annotated[Headers, Header()]
):
    return {"headers": headers}

@router.post('/test03/')
async def test03(
    item: Item
) -> Item:
    return item

@router.post('/test04/')
async def test04() -> list[Item]:
    return [
        Item(name='Foo', description='The Foo is a good item', price=10.0, tax=1.0),
        Item(name='Bar', description='The Bar is a good item', price=20.0, tax=2.0)
    ]

@router.post('/test05/', response_model=UserOut)
async def create_user(
    user: UserIn
) -> Any:
    return user