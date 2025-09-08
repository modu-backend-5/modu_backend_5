from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
items = []


class Item(BaseModel):
    name: str
    price: float = 0


@app.get("/item")
async def item_list():
    return {"items": items}

@app.post("/item")
async def item_create(item: Item):
    items.append(item)
    return {"item": item}