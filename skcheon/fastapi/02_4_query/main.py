from fastapi import FastAPI

app = FastAPI()

# items = [
#     {"item_id": "Foo"},
#     {"item_id": "Bar"},
#     {"item_id": "Baz"},
#     {"item_id": "Qux"},
#     {"item_id": "Quux"},
#     {"item_id": "Corge"},
#     {"item_id": "Grault"},
#     {"item_id": "Garply"},
#     {"item_id": "Waldo"},
#     {"item_id": "Fred"},
#     {"item_id": "Plugh"},
#     {"item_id": "Xyzzy"},
#     {"item_id": "Thud"},
#     {"item_id": "A"},
#     {"item_id": "B"},
#     {"item_id": "C"},
#     {"item_id": "D"},
#     {"item_id": "E"},
#     {"item_id": "F"},
#     {"item_id": "G"},
#     {"item_id": "H"},
#     {"item_id": "I"},
#     {"item_id": "J"},
#     {"item_id": "K"},
#     {"item_id": "L"},
#     {"item_id": "M"},
#     {"item_id": "N"},
#     {"item_id": "O"},
#     {"item_id": "P"},
#     {"item_id": "Q"},
#     {"item_id": "R"},
#     {"item_id": "S"},
#     {"item_id": "T"},
#     {"item_id": "U"},
#     {"item_id": "V"},
#     {"item_id": "W"},
#     {"item_id": "X"},
#     {"item_id": "Y"},
#     {"item_id": "Z"},
# ]

# @app.get("/items")
# def read_items(skip: int = 0, limit: int = 10):
#     return_items = items[skip : skip + limit]
#     # return {"skip": skip, "limit": limit}
#     return {"return_items": return_items}

# @app.get("/items")
# def read_items(
#     skip: int,
# ):
#     return {"skip" : skip}

# @app.get("/items")
# def read_items(item_id: int, q: str | None = None):
#     item = items[item_id]
#     if q:
#         item.update({"q": q})   # item dict에 q key, value 추가
#     return {"item": item}

# @app.get("/items")
# def read_items(item_id: bool):
#     print(f"item_id: {item_id} / type: {type(item_id)}")
    
items = [
    {"name": "item1", "price": 1000, "available": True},
    {"name": "item2", "price": 2000, "available": False},
    {"name": "item3", "price": 3000, "available": True},
    {"name": "item4", "price": 4000, "available": False},
    {"name": "item5", "price": 5000, "available": True},
    {"name": "item6", "price": 6000, "available": False},
    {"name": "item7", "price": 7000, "available": True},
    {"name": "item8", "price": 8000, "available": False},
    {"name": "item9", "price": 9000, "available": True},
    {"name": "item10", "price": 10000, "available": False},
]

# 페이지네이션 구현
@app.get("/list")
def item_paging(page: int = 1, size: int = 10):
    item_page = items[(page - 1) * size : page * size]
    return {"item_page": item_page}

# 상품 검색 API
@app.get("/search")
def item_search(name: str | None = None, min_price: int | None = None, max_price: int | None = None, available: bool | None = None):
    result = items
    if name is not None:
        result = [item for item in result if name in item["name"]]
    if min_price is not None:
        result = [item for item in result if item["price"] >= min_price]
    if max_price is not None:
        result = [item for item in result if item["price"] <= max_price]
    if available is not None:
        result = [item for item in result if item["available"] == available]
    
    return {"result": result}

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 22},
    {"name": "Frank", "age": 33},
    {"name": "Grace", "age": 27},
    {"name": "Heidi", "age": 29},
    {"name": "Ivan", "age": 31},
    {"name": "Judy", "age": 26}
]

# 사용자 목록 반환 API
@app.get("/users")
def get_users(page: int = 1, size: int = 10, sort_by: str = "name"):
    sorted_users = sorted(users, key=lambda x: x[sort_by])
    paged_users = sorted_users[(page-1)*size : page*size]
    return {"paged_users" : paged_users}