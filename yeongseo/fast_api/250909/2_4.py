from typing import Optional
from fastapi import FastAPI

app=FastAPI()

# @app.get('/items')
# def read_items(skip:int=0, limit: int=10):
#     return {'skip':skip, "limit":limit}

# @app.get('/items')
# def read_items(hello: str='world', limit: int=10):
#     return {'hello':hello, "limit":limit}


# @app.get("/items")
# def read_item(item_id:int):
#     return {'item_id':item_id}


# @app.get('/items')
# def read_items(item_id:int, q: Optional[str] = None):
#     results= {'item_id': item_id}
#     if q:
#         results.update({'q':q})
#     return results

# -------------------------------------
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

@app.get('/items')
def read_items(page:int=1, size:int=10):
    return_items=items[(page-1)*size:page*size]
    return return_items

@app.get('/products')
def search_product(name:str|None= None,
                   min_price:int|None= None,
                   max_price:int|None= None,
                   available:bool|None= None,):
    return_items=items
    if name:
        return_items=[item for item in return_items if name in item.get('name')]
    if min_price:
        return_items=[item for item in return_items if item.get('price')>=min_price]
    if max_price:
        return_items=[item for item in return_items if item.get('price')<=max_price]
    if available:
        return_items=[item for item in return_items if item.get('available')==available]
    return_items=return_items if not len(return_items)==0 else '조건에 맞는 상품이 없습니다.'
    return {'return_items': return_items}    


users = [
    {'name': 'user03', 'age': 48},
    {'name': 'user19', 'age': 54},
    {'name': 'user01', 'age': 25},
    {'name': 'user02', 'age': 31},
    {'name': 'user15', 'age': 54},
    {'name': 'user06', 'age': 50},
    {'name': 'user16', 'age': 56},
    {'name': 'user05', 'age': 38},
    {'name': 'user12', 'age': 46},
    {'name': 'user18', 'age': 49},
    {'name': 'user07', 'age': 33},
    {'name': 'user04', 'age': 38},
    {'name': 'user20', 'age': 59},
    {'name': 'user13', 'age': 53},
    {'name': 'user11', 'age': 58},
    {'name': 'user09', 'age': 49},
    {'name': 'user17', 'age': 55},
    {'name': 'user08', 'age': 37},
    {'name': 'user10', 'age': 19},
    {'name': 'user14', 'age': 56},
]



@app.get('/users')
def read_users(page: int=1, size: int=10, sort_by: str='name'):
    return_user=sorted(users, key=lambda x: x.get(sort_by))
    return_user=return_user[(page-1)*(size):(page)*(size)]
    return return_user

