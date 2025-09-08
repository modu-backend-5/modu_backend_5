from fastapi import FastAPI

app=FastAPI()

@app.get('/blog/{post_id}')
def blog_detail(post_id:int):
    return {'게시글 번호':post_id+post_id}


@app.get('/blog/{post_tag}/{post_author}')
def tag_author_list(post_tag:str, post_author: str):
    return {"태그":post_tag,"저자":post_author}

@app.get('/')
def index(name:str, price:int):
    return {'name':name, 'price':price}



from models import Item

items=[]

@app.get('/item')
def item_list():
    return {"items":items}



# @app.post('/item')
# def item_create(item:dict):
#     items.append(item)
#     return {'item':item}

@app.post('/item')
def item_create(item:Item):
    items.append(item)
    return {'item':item}


@app.get('/item/{item_id}')
def item_detail(item_id:int):
    try:
        item=items[item_id-1]
    except IndexError:
        return {'error': "Item not found"}
    return {'item':item}

@app.put('/item/{item_id}')
def item_update(item_id:int, item:Item):
    items[item_id-1]=item
    return {'item': item}

# -------------------------

from models import User, BlogPost

users=[]

@app.get('/user')
def user_list():
    return {'users':users}

@app.post('/user')
def create_user(user:User):
    users.append(user)
    return {"user":user}


blog_posts=[]


@app.get('/blogposts')
def blogpost_list():
    return {'blogpost': blog_posts}
    
@app.post('/blogposts')
def create_blogpost(blogpost: BlogPost):
    blog_posts.append(blogpost)
    return {'blogpost':blogpost}
