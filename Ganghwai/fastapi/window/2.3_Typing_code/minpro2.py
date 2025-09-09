# 블로그 포스트를 생성하는 엔드포인트를 만들어보세요. 블로그 포스트는 제목, 내용, 작성자 정보(이름, 이메일)를 포함해야 합니다. 중첩된 Pydantic 모델을 사용하세요.

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 메모리에 데이터 저장
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
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "안녕하세요!"}


@app.post("/users")
def create_user(user: User):
    user_data = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }
    users.append(user_data)
    return user_data


@app.get("/users")
def get_users():
    return users


@app.post("/posts")
def create_post(post: BlogPost):
    post_data = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content,
        "author": {"name": post.author.name, "email": post.author.email},
    }
    posts.append(post_data)
    return post_data


@app.get("/posts")
def get_posts():
    return posts


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
