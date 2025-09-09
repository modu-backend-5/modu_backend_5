from pydantic import BaseModel, ValidationError, field_validator
from typing import List

class User(BaseModel):
    # name: str
    id: int
    username: str
    # age: int
    email: str
    password: str | None = None
    # hobbies: List[str] | None = None # 선택적 필드. 기본값 None

    # @field_validator("name")
    # @classmethod
    # def validate_name(cls, name: str) -> str:
    #     if len(name) < 2:
    #         raise ValueError("이름은 최소 2자 이상이어야 합니다.")
    #     return name

    # 나이 유효성 검사
    # 1 이상이어야 함
    # @field_validator("age")
    # @classmethod
    # def validate_age(cls, age: int) -> int:
    #     if age < 1:
    #         raise ValueError("나이는 1 이상이어야 합니다.")
    #     return age
    
    # 이메일 유효성 검사
    # @가 포함되어 있어야 함
    # @field_validator("email")
    # @classmethod
    # def validate_email(cls, email:str) -> str:
    #     if "@" not in email:
    #         raise ValueError("유효한 이메일 주소가 아닙니다.")
    #     return email
    
class Item(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    
class Message(BaseModel):
    status_code: int = 200
    message: str