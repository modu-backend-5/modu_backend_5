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

# password 필드를 제외한 사용자 정보 반환 API
@app.get("/users")
def read_users():
    return {"users": [user.dict(exclude={"password"}) for user in users]}

# item 생성
# 정상 생성의 경우 201 응답 코드 반환
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"item": item}
    # return Response(status_code=status.HTTP_201_CREATED)

@app.get("/items")
def read_items():
    return {"items": items}

@app.get("/items/mode/{mode}")
def read_items_mode(mode: int = 0, response_model=Union[dict, dict]):
    exclude_fields = {"stock"} if mode == 0 else None
    return {"items" : [item.dict(exclude=exclude_fields) for item in items]}
    # if mode == 0:
    #     return {"기본 모드": [item.dict(exclude={"stock"}) for item in items]}
    # return {"상세 모드": items}

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     if item_id < 0 or item_id >= len(items):
#         raise HTTPException(status_code=404, detail="찾으시는 아이템이 없습니다.")
#     return {"item": items[item_id]}

# @app.get("/items/{item_id}", response_model= Union[Item, Message])
# def read_item(item_id: int):
#     if item_id < 0 or item_id >= len(items):
#         return Message(message="찾으시는 아이템이 없습니다.")
#     return items[item_id]