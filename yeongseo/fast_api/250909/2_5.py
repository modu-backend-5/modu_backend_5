from typing import List, Union
from fastapi import FastAPI, Response, status
from models import  ProductDetail, ProductStandard, User

app=FastAPI()


users=[
    {'user_id': 1, 'username': 'user1', 'email': 'user1@example.com', '__password': 'pass123'},
    {'user_id': 2, 'username': 'user2', 'email': 'user2@example.com', '__password': 'secret456'},
    {'user_id': 3, 'username': 'user3', 'email': 'user3@example.com', '__password': 'abc789'},
    {'user_id': 4, 'username': 'user4', 'email': 'user4@example.com', '__password': 'mypassword'},
    {'user_id': 5, 'username': 'user5', 'email': 'user5@example.com', '__password': 'qwerty123'}
]


# @app.get('/users/{user_id}', response_model=User)
# def read_users(user_id: int):
#     for user in users:
#         if user.get('user_id')==user_id:
#             return user
#     return Response(status_code=status.HTTP_404_NOT_FOUND, content='존재하지 않는 아이디 입니다.')


@app.get('/users', response_model=List[User])
def read_users():
    return users





products = [
    {"product_id": 1, "name": "Laptop", "price": 1200, "stock": 10},
    {"product_id": 2, "name": "Mouse", "price": 25, "stock": 50},
    {"product_id": 3, "name": "Keyboard", "price": 70, "stock": 20},
    {"product_id": 4, "name": "Monitor", "price": 300, "stock": 15},
    {"product_id": 5, "name": "USB Cable", "price": 10, "stock": 100},
    {"product_id": 6, "name": "Webcam", "price": 80, "stock": 25},
    {"product_id": 7, "name": "Headset", "price": 60, "stock": 30},
    {"product_id": 8, "name": "Chair", "price": 150, "stock": 5},
    {"product_id": 9, "name": "Desk", "price": 200, "stock": 7},
    {"product_id": 10, "name": "Notebook", "price": 5, "stock": 200},
]




# @app.get('/products', response_model=List[ProductList])
# def products_list(mode: bool= False):
#     '''False는 기본 모드, True는 상세모드'''
#     if mode== False:
#         return_product=[{x: y[x] for x in ["product_id","name","price"]} for y in products]
#         return return_product
#     return products
    
    

@app.get('/products', response_model=Union[List[ProductStandard],List[ProductDetail]])
def products_list(mode: bool=False):
    '''False는 기본 모드, True는 상세모드'''
    if mode ==False:
        return_product=[{x: y[x] for x in ["product_id","name","price"]} for y in products]
        return return_product
    return products