# 연습문제 1
# 상품 목록 리스트를 만들어서 페이지네이션을 구현.
# API는 다음과 같은 쿼리 매개변수를 받아야 함

from fastapi import FastAPI

app = FastAPI()

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

@app.get("/pages")
def page_number(page: int = 1, size: int = 10):
    start = (page - 1) * size
    return items[start:start + size]


@app.get("/search")
def search_item(name: str, min_price:  int, max_price: int, available: bool):
    pass


@app.get("/users")
def user_list(page: int = 1, size: int = 10, sort_by: str = "name"):
    pass

# 수업 내용 놓친걸 공부하다보니 시간이 부족햇습니다ㅠ