from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemDetail(BaseModel):
    description: str
    weight: float
 
class Item(BaseModel):
    name: str
    price: float
    details: ItemDetail

@app.get("/")
def index(name:str, price:int):
    print(name, price)
    return {"name": name, "price": price}

items = []
 
 
@app.get("/item")
def item_list():
    return {"items": items}
 
 
@app.post("/item")
def item_create(item: Item):
    items.append(item)
    return {"item": item}

@app.get("/item/{item_id}")
def item_detail(item_id: int):
    try:
        item = items[item_id - 1]
    except IndexError:
        return {"error": "Item not found"}
    return {"item": item}
 
 
@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}