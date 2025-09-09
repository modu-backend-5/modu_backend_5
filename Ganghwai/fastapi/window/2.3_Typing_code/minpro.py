from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

app = FastAPI()


users = []
posts = []


class User(BaseModel):
    user_id: int
    name: str
    email: str
    age: int


class Author(BaseModel):
    name: str
    email: str


class BlogPost(BaseModel):
    title: str
    content: str
    author: Author


@app.get("/")
def home():
    # import 에러
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "안녕하세요! 간단한 블로그 API입니다."}


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user


@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/posts")
def create_post(post: BlogPost):
    posts.append(post)
    return post


@app.get("/posts")
def get_posts():
    return {"posts": posts}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
