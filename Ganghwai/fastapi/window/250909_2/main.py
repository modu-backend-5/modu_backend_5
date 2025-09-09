from typing import List, Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class ProductBasic(BaseModel):
    id: int
    name: str
    price: float


class ProductDetail(ProductBasic):
    stock: int


class UserInDB(BaseModel):
    id: int
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str


fake_products = [
    {"id": 1, "name": "Laptop", "price": 1200.0, "stock": 5},
    {"id": 2, "name": "Mouse", "price": 25.5, "stock": 100},
    {"id": 3, "name": "Keyboard", "price": 75.0, "stock": 50},
]

fake_users_db = [
    UserInDB(id=1, username="alice", email="alice@example.com", password="hashed_pw1"),
    UserInDB(id=2, username="bob", email="bob@example.com", password="hashed_pw2"),
]


@app.get("/users", response_model=List[UserResponse])
def get_users():

    return fake_users_db


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


@app.get("/products", response_model=List[ProductBasic])
def get_products(mode: Optional[str] = Query("basic", description="basic 또는 detail")):
    if mode == "detail":
        return [ProductDetail(**p) for p in fake_products]
    return [ProductBasic(**p) for p in fake_products]
