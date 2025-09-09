from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int = None


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# 사용자 정보를 저장하는 POST 엔드포인트를 만들어보세요. 사용자 정보는 이름, 이메일, 나이를 포함해야 합니다. Pydantic 모델을 사용하여 데이터를 검증하세요.

# 블로그 포스트를 생성하는 엔드포인트를 만들어보세요. 블로그 포스트는 제목, 내용, 작성자 정보(이름, 이메일)를 포함해야 합니다. 중첩된 Pydantic 모델을 사용하세요.

users = []


@app.post("/users")
def register(user: User):
    if "@" not in user.email:
        return {"error": "잘못된 이메일"}
    users.append(user)
    return {"message": "가입완료", "user": user}


class BlogPost(BaseModel):
    title: str
    content: str
    author: User


class BlogPostResponse(BaseModel):
    id: int
    email: str
    details: BlogPost


posts = []


# class BlogPost(BaseModel):
#     title: str
#     content: str
#     author: User
@app.post("/blogs")
def create_blog_post(blog_post: BlogPost):
    # 이미 검증된 user
    # if "@" not in blog_post.author.email:
    #     return {"error": "잘못된 이메일"}
    posts.append(blog_post)
    {"title": blog_post.title, "content": blog_post.content, "author": blog_post.author}
    response_post = BlogPostResponse(blog_post.model_dump())
    return {"message": "가입완료", "blog_post": response_post}
