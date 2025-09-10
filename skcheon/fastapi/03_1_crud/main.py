from typing import List, Optional, Union
from fastapi import FastAPI, Response, status, HTTPException
from models import Item

app = FastAPI(
    title="CRUD 앱",
    description="CRUD 기능을 구현한 FastAPI 앱입니다",
    version="1.0.0"
)

items = []

# 아이템 생성
@app.post("/items", response_model=Item, tags=["Items"])
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

# 아이템 조회
@app.get("/items")
def read_items(skip: int = 0, limit: int = 10, tags=["Items"]):
    # TODO: items가 비어있을 경우 에러 반환        
    return_items = items[skip : skip + limit]
    if not return_items:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="조회된 아이템이 없습니다."
        )
    
    return return_items

# 아이템 업데이트
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, response_model=Item, tags=["Items"]):
    # item_id 예외 처리
    if item_id < 0 or item_id >= len(items):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 아이템입니다."
        )
    
    # 업데이트
    items[item_id] = item
    
    return item

# put과 fetch의 차이점
# put은 전체 업데이트, fetch는 부분 업데이트
# put은 전체 데이터를 보내야 하지만, fetch는 변경할 데이터만 보내면 됨

# 아이템 삭제
@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int):
    # item_id 예외 처리
    if item_id < 0 or item_id >= len(items):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 아이템입니다."
        )
    
    # 삭제
    # del items[item_id]
    # items.remove(items[item_id])
    # items.pop(item_id)
    deleted_item = items.pop(item_id)
    return deleted_item

# 특정 단어가 이름에 포함된 경우 삭제하는 API
@app.delete("/items")
def delete_items_by_name(name: Optional[str] = None, tags=["Items"]):
    # 요청 받았는데 쿼리 파라미터로 name이 없는 경우
    if name is None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="name 쿼리 파라미터가 필요합니다."
        )
    
    # name이 있는 경우
    # items 리스트에서 item 요소들 중 name이 쿼리 파라미터로 전달된 name을 포함하는 경우 삭제
    deleted_items = list(filter(lambda item: name in item.name, items))
    
    for item in deleted_items:
        items.remove(item)
    
    return {"deleted_items": deleted_items}
    