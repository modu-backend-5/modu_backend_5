from typing import Union
from fastapi import FastAPI, Response, status
from models import User, Item, Message

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

users = []
items = []

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"user": user}

# item 생성
# 정상 생성의 경우 201 응답 코드 반환
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return Response(status_code=status.HTTP_201_CREATED)

@app.get("/items")
def read_items():
    return {"items": items}

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id < 0 or item_id >= len(items):
#         raise HTTPException(status_code=404, detail="찾으시는 아이템이 없습니다.")
#     return {"item": items[item_id]}

@app.get("/items/{item_id}", response_model= Union[Item, Message])
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return Message(message="찾으시는 아이템이 없습니다.")
    return items[item_id]