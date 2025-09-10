from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

items = []

# Pydantic model 정의
class Item(BaseModel):
    name: str
    price: float

@app.post(
    "/item/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude={"price"},
)
def create_item(item: Item):
    items.append(item)
    return item
 
 
@app.get("/item/")
def read_items():
    return items
 
 
@app.get("/item/{item_id}")
def read_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")



# # 메모리에 데이터를 저장할 리스트
# items = []

# @app.post("/item/", status_code=404)
# def create_item(item: Item):
#     items.append(item)
#     return {"message": "Item created successfully", "item": item}
 
 
# @app.get("/item/")
# def read_items():
#     return items
 
 
# @app.get("/item/{item_id}")
# def read_item(item_id: int):
#     if 0 <= item_id < len(items):
#         return items[item_id]
#     raise HTTPException(status_code=404, detail="Item not found")




# @app.post("/item/")
# def create_item(item: Item):
#     items.append(item)
#     return {"message": "Item created successfully", "item": item}


# @app.get("/item/")
# def read_items():
#     return items


# @app.get("/item/{item_id}")
# def read_item(item_id: int):
#     if 0 <= item_id < len(items):
#         return items[item_id]
#     raise HTTPException(status_code=404, detail="Item not found")



# from pydantic import BaseModel, ValidationError
# from typing import List

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     hobbies: List[str] | None = None

# def validate_user(user_data: dict) -> User:
#     try:
#         return User(**user_data)
#     except ValidationError as e:
#         print(f"유효성 검사 오류: {e}")
#         return None
    
# # 올바른 데이터
# valid_data = {
#     "name": "홍길동",
#     "age": 30,
#     "email": "hong@example.com",
#     "hobbies": ["독서", "등산"]
# }

# # 잘못된 데이터
# invalid_data = {
#     "name": "김철수",
#     "age": "스물다섯", #문자열로 잘못 입력
#     "email": "invalid-email", # 올바르지 않은 이메일 형식
#     "hobbies": "독서" # 문자열 대신 리스트
# }

# # 올바른 데이터로 사용자 생성
# user = validate_user(valid_data)
# if user:
#     print("유효한 사용자:", user)
#     print("직렬화된 사용자:", user.model_dump())

# # 잘못된 데이터로 사용자 생성 시도
# invalid_user = validate_user(invalid_data) 



