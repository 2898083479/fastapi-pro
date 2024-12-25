from fastapi import FastAPI, Query, Path
from typing import Annotated, List, Literal
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post('/items/')
async def update_item(
        item: Annotated[Item, Query()],
        allow_update: Annotated[bool, Query(description='Allow update of the item')] = False
    ):
    result = {"name": item.name, "description": item.description, "price": item.price, "tax": item.tax}
    if allow_update:
        result.update({"allow_update": allow_update})
    return result