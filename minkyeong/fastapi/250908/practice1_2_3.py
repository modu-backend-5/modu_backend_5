# 1. 사용자 정보를 저장하는 POST 엔드포인트
# 사용자 정보: 이름, 이메일, 나이를 포함. Pydantic 모델을 사용하여 데이터를 검증

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    name: str
    email: str
    age: int

@app.get("/user")
def user_list():
    return {"users": users}

@app.post("/user")
def user_info(user: User):
    users.append(user)
    return {"user": user}