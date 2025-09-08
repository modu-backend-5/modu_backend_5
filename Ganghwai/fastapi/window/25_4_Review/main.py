from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()
users = []
posts = []


class User(BaseModel):
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
    return FileResponse("index.html")


@app.post("/users")
def create_user(user: User):
    user_data = {"id": len(users) + 1, **user.dict()}
    users.append(user_data)
    return user_data


@app.post("/posts")
def create_post(post: BlogPost):
    post_data = {"id": len(posts) + 1, **post.dict()}
    posts.append(post_data)
    return post_data
