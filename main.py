from fastapi import FastAPI, Query, Path
from typing import Annotated, List, Literal
from pydantic import BaseModel, Field


app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    name: str = Field('', description='The name of the item to filter by'),
    tags: List[str] = Field([], description='The tags of the item to filter by')


@app.get('/index')
def index():
    return {'message': 'Hello, World!'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id: int,
        item_id: int,
        p: str | None = None,
        short: bool = False
):
    item = {'user_id': user_id, 'item_id': item_id}
    if not short:
        item.update({'description': f'This is item {item_id}'})
    if p:
        return {'item': item, 'p': p}
    return item


class Item(BaseModel):
    name: str
    eventId: int
    description: str | None = None

@app.post('/items')
async def create_item(item: Item):
    return item

@app.get('/hello')
async def hello():
    return {'message': 'Hello, World!'}

@app.get('/test1')
async def test1(q: str = Query(default=None, min_length=3, max_length=10)):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

@app.get('/test2')
def test2(q: Annotated[str | None, Query(min_length=1, max_length=5, pattern='^[a-z]+$')]):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

@app.get('/test3')
def test3(q: Annotated[List[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

@app.get('/test4')
def test4(q: Annotated[str | None, 
Query(
    title='Query string',
    description='Query string for the items to search in the database that have a good match',
    min_length=3,
    max_length=10,
    alias='item-query',
    deprecated=True,
)] = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

@app.get('/test/{item_id}')
def test5(
    item_id: Annotated[int, Path(title='The ID of the item to get')],
    q: Annotated[str | None, Query(title='Query string', description='Query string for the items to search in the database that have a good match')] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get('/test6/{item_id}')
def test6(
    item_id: Annotated[int, Path(title='The ID of the item to get', ge=1, description='The ID of the item to get', deprecated=True)],
    size: Annotated[float, Query(gt=1.1, lt=100.0)]
):
    results = {"item_id": item_id}
    if size:
        results.update({"size": size})
    return results

@app.get('/test7')
async def test7(filter_params: Annotated[FilterParams, Query()]):
    return filter_params

