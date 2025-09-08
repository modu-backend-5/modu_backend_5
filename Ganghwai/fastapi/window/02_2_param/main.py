from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()


posts = [
    {"id": 1, "title": "First Post"},
    {"id": 2, "title": "Second Post"},
    {"id": 3, "title": "Third Post"},
    {"id": 4, "title": "Fourth Post"},
    {"id": 5, "title": "Fifth Post"},
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/blog")
def blog_list():
    return {"posts": posts}


@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    print(type(post_id))
    return {"post": post_id}


posts = [
    {"id": 1, "title": "First Post", "tag": "fastapi", "author": "천수겸"},
    {"id": 2, "title": "Second Post", "tag": "python", "author": "장민경"},
    {"id": 3, "title": "Third Post", "tag": "backend", "author": "mr. kim"},
    {"id": 4, "title": "Fourth Post", "tag": "fastapi", "author": "신가람"},
    {"id": 5, "title": "Fifth Post", "tag": "backend", "author": "경환"},
    {"id": 6, "title": "Sixth Post", "tag": "backend", "author": "경환"},
    {"id": 7, "title": "Seventh Post", "tag": "backend", "author": "경환"},
    {"id": 8, "title": "Eighth Post", "tag": "backend", "author": "경환"},
]

if __name__ == "__main__":
    result = get_posts()
    print(result)

    for post in result:
        print(f"ID: {post['id']}, Title: {post['title']}")


@app.get("/blog/{post_id}")
def blog_detail(post_id: int):
    filtered_post = [post for post in posts if post["id"] == post_id]
    return {"post": filtered_post[0]}


@app.get("/blog/tag/{post_tag}")
def blog_tag_list(post_tag: str):
    filtered_post = []
    for post in posts:
        if post["tag"] == post_tag:
            filtered_post.append(post)
    return {"filtered_post": filtered_post}


# GET /blog/tag/fastapi/경환
# post_tag = fastapi
# post_author = 경환
# [{"id": 4, "title": "Fourth Post", "tag": "fastapi", "author": "경환"}]
#
@app.get("/blog/tag/{post_tag}/{post_author}")
def blog_tag_author_list(post_tag: str, post_author: str):
    filtered_posts = []
    for post in posts:
        if post["tag"] == post_tag and post["author"] == post_author:
            filtered_posts.append(post)
    return {"filtered_posts": filtered_posts}
