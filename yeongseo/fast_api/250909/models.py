from typing import Optional
from pydantic import BaseModel, field_validator

# class User(BaseModel):
#     user_id: int
#     username: str
#     email: str
#     __password : str


class User(BaseModel):
    user_id: int
    username: str
    email: str
    
    
    
# class ProductList(BaseModel):
#     product_id: int
#     name: str
#     price: float
#     stock : Optional[int]=None

    
class ProductStandard(BaseModel):
    product_id: int
    name: str
    price: float


class ProductDetail(ProductStandard):
    stock : int
    
    
    