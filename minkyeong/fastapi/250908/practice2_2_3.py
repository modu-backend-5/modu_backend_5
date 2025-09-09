# 2 블로그 포스트를 생성하는 엔드포인트 만들기
# 블로그 포스트는 제목, 내용, 작성자 정보(이름, 이메일)를 포함
# 중첩된 Pydantic 모델을 사용

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
posts = []
# users = [Userinfo, Userinfo]
# users.append(user)
users = []


class Userinfo(BaseModel):
    name: str
    email: str


class Userpost(BaseModel):
    title: str
    contents: str
    author: Userinfo


@app.get("/blogpost")
def post_():
    return {"posts": posts}


@app.post("/blogpost")
def create_post(post: Userpost):
    posts.append(post)
    return {"post": post}


@app.post("/user")
def create_user(user: Userinfo):
    users.append(user)
    return {"user": user}


@app.get("/user/{user_id}")
def user_info(user_id: int):
    find_user = users[user_id]
    return {"find_user": find_user}


# @app.post("/user")
# def create_user(user: Userinfo):
#     users.append(user)
#     return {"user": user}
