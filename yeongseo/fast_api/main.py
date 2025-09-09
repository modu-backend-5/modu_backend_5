from fastapi import FastAPI
from .item_router import router as item_router

app = FastAPI()

app.include_router(item_router, prefix="/items", tags=["items"])


@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    return {"게시글 번호": post_id + post_id}


@app.get("/blog/{post_tag}/{post_author}")
def tag_author_list(post_tag: str, post_author: str):
    return {"태그": post_tag, "저자": post_author}


@app.get("/")
def index(name: str, price: int):
    return {"name": name, "price": price}


from models import Item

items = []


@app.get("/item")
def item_list():
    return {"items": items}


# @app.post('/item')
# def item_create(item:dict):
#     items.append(item)
#     return {'item':item}


@app.post("/item")
def item_create(item: Item):
    items.append(item)
    return {"item": item}


@app.get("/item/{item_id}")
def item_detail(item_id: int):
    try:
        item = items[item_id - 1]
    except IndexError:
        return {"error": "Item not found"}
    return {"item": item}


@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}


# -------------------------
# 사용자 정보를 저장하는 POST 엔드포인트를 만들어보세요. 사용자 정보는 이름, 이메일, 나이를 포함해야 합니다. Pydantic 모델을 사용하여 데이터를 검증하세요.

# 블로그 포스트를 생성하는 엔드포인트를 만들어보세요. 블로그 포스트는 제목, 내용, 작성자 정보(이름, 이메일)를 포함해야 합니다. 중첩된 Pydantic 모델을 사용하세요.
from models import User, BlogPost

users = []


@app.get("/users")
def user_list():
    return {"users": users}


# @app.get("/users/{user_id}")
@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"user": user}


blog_posts = []


@app.get("/blogposts")
def blogpost_list():
    return {"blogpost": blog_posts}


@app.post("/blogposts")
def create_blogpost(blogpost: BlogPost):
    blog_posts.append(blogpost)
    return {"blogpost": blogpost}
