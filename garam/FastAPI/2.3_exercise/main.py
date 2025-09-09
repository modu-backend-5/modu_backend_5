from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int = None


@app.get("/test")
def test():
    return {"서버작동중"}


@app.post("/register")
def register(user: User):
    if "@" not in user.email:
        return {"error": "잘못된 이메일"}
    return {"message": "가입완료", "user": user}


class BlogPost(BaseModel):
    title: str
    content: str
    author: str


class BlogPostResponse(BaseModel):
    id: int
    email: str
    details: BlogPost


@app.post("/blog/register")
def create_blog_post(blog_post: BlogPost):
    if "@" not in blog_post.email:
        return {"error": "잘못된 이메일"}
    return {"message": "가입완료", "blog_post": blog_post}
