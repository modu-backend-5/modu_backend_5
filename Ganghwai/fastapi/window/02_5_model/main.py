from fastapi import FastAPI, HTTPException
from models import Item, User, message
from typing import Union

app = FastAPI()

users = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


items = []

message = []


@app.post("/items")
@app.post("/items")
def create_item(
    user: User,
):
    users.append(user)
    return {"user": user}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return


@app.get("/items")
def read_items():
    return {"items": items}


# items = [Item instance, Item instance, Item instance]
# -1, 4 -> 404
@app.get("/items/{item_id}")
def read_items(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="찾으시는 아이템이 없습니다.")
    return {"item": items[item_id]}


@app.get("/items/{item_id}", response_model=Union[Item, Message])
def read_items(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return Message(message="찾으시는 아이템이 없습니다.")
    return items[item_id]
