from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/item")
async def item_list():
    return {"items": items}


@app.post("/item")
async def item_create(item: dict):
    items.append(item)
    return {"item": item}