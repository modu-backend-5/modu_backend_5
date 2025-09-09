from typing import List
from fastapi import FastAPI, Response, status
from models import Item

app = FastAPI()

items = []

@app.post("/items", response_model=Item)
def create_item(item: Item):
    for existing_item in items:
        if existing_item.name == item.name:
            # raise ValueError("이미 존재하는 아이템 이름입니다.")
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                content="이미 존재하는 아이템 이름입니다."
            )
    items.append(item)
    return item

@app.get("/items", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return_items = items[skip : skip + limit]
    return return_items