from fastapi import FastAPI, Query, Path, Body, APIRouter
from typing import Annotated, List, Literal
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, time, date, timedelta

router = APIRouter(
    prefix='/test1', tags=['test1 API']
)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@router.post('/items/')
async def update_item(
        item: Annotated[Item, Query()],
        allow_update: Annotated[bool, Query(description='Allow update of the item')] = False
    ):
    result = {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}
    if allow_update:
        result.update({"allow_update": allow_update})
    return result

@router.put('/items/{item_id}')
async def update_item(
    item_id: Annotated[int, Path(title='The ID of the item to get')],
    item: Annotated[Item,
                    Body(
                        example=[
                            {
                                "name": "Foo",
                                "description": "The Foo is a good item",
                                "price": 10.0,
                                "tax": 1.0
                            }
        ]
    )]
):
    results = {"item_id": item_id, "item": item}
    return results