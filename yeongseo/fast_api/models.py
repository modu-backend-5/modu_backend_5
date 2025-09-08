from pydantic import BaseModel


class ItemDetail(BaseModel):
    description: str
    weight: float


class Item(BaseModel):
    name: str
    price:float =0
    details: ItemDetail
    
    
    
class User(BaseModel):
    name: str
    email: str
    age: int
    

class UserDetail(BaseModel):
    name: str
    email: str
    
class BlogPost(BaseModel):
    title:str
    detail: str
    user_detail: UserDetail