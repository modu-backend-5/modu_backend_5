# 2 블로그 포스트를 생성하는 엔드포인트 만들기
# 블로그 포스트는 제목, 내용, 작성자 정보(이름, 이메일)를 포함
# 중첩된 Pydantic 모델을 사용

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
posts = []

class Userpost(BaseModel):
    title: str
    contents: str

class Userinfo(BaseModel):
    name: str
    email: str


@app.get("/blogpost")
def post_():
    return {"posts": posts}

@app.post('/blogpost')
def create_post(post: Userpost):
    posts.append(post)
    return {"post": post}


@app.get("/blogpost/{user_id}")
def user_info(user_id: int):
    return {"user_id": user_id}

@app.post("/blogpost/{user_id}")
def user_info(user_id: int):
    posts.append() # ???ㅠㅜㅠ