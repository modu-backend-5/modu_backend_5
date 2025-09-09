# 상품 목록 리스트를 만들어서 페이지네이션을 구현해보세요. 이 API는 다음과 같은 쿼리 매개변수를 받아야 합니다.


from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List
import math

app = FastAPI()


items = [
    {"id": 1, "name": "item1", "price": 1000, "available": True},
    {"id": 2, "name": "item2", "price": 2000, "available": False},
    {"id": 3, "name": "item3", "price": 3000, "available": True},
    {"id": 4, "name": "item4", "price": 4000, "available": False},
    {"id": 5, "name": "item5", "price": 5000, "available": True},
    {"id": 6, "name": "item6", "price": 6000, "available": False},
    {"id": 7, "name": "item7", "price": 7000, "available": True},
    {"id": 8, "name": "item8", "price": 8000, "available": False},
    {"id": 9, "name": "item9", "price": 9000, "available": True},
    {"id": 10, "name": "item10", "price": 10000, "available": False},
]


class User(BaseModel):
    id: int
    name: str
    email: str


class Item(BaseModel):
    id: int
    name: str
    price: int
    available: bool


class PaginationResponse(BaseModel):
    items: List[Item]
    total: int
    page: int
    size: int
    total_pages: int
    has_next: bool
    has_previous: bool


@app.get("/items", response_model=PaginationResponse)
def get_items(
    page: int = Query(1, ge=1, description="현재 페이지 번호"),
    size: int = Query(10, ge=1, le=100, description="한 페이지당 상품 개수"),
    available: Optional[bool] = Query(None, description="재고 상태로 필터링"),
):
    """
    상품 목록을 페이지네이션으로 조회합니다.
    """

    filtered_items = items
    if available is not None:
        filtered_items = [item for item in items if item["available"] == available]

    total = len(filtered_items)

    total_pages = math.ceil(total / size)

    start_index = (page - 1) * size
    end_index = start_index + size

    current_page_items = filtered_items[start_index:end_index]

    has_previous = page > 1
    has_next = page < total_pages

    return PaginationResponse(
        items=current_page_items,
        total=total,
        page=page,
        size=size,
        total_pages=total_pages,
        has_next=has_next,
        has_previous=has_previous,
    )


@app.get("/")
def home():
    return {"message": "상품 페이지네이션 API"}


fake_users = [
    User(id=1, name="웅이", email="alice@example.com"),
    User(id=2, name="옹이", email="bob@example.com"),
    User(id=3, name="콩이", email="charlie@example.com"),
    User(id=4, name="야옹", email="david@example.com"),
    User(id=5, name="멍멍", email="eve@example.com"),
]


@app.get("/users", response_model=List[User])
def get_users(
    page: int = Query(1, ge=1, description="페이지 번호 (1 이상)"),
    limit: int = Query(10, ge=1, le=100, description="한 페이지당 항목 수"),
    search: Optional[str] = Query(None, description="사용자 이름 검색"),
    sort_by: Optional[str] = Query(
        "id", description="정렬 기준 필드 (id, name, email)"
    ),
    order: Optional[str] = Query("asc", description="정렬 순서 (asc, desc)"),
):

    users = fake_users
    if search:
        users = [u for u in users if search.lower() in u.name.lower()]

    if sort_by in {"id", "name", "email"}:
        users.sort(key=lambda x: getattr(x, sort_by), reverse=(order == "desc"))

    start = (page - 1) * limit
    end = start + limit
    return users[start:end]
