from fastapi import FastAPI
from typing import Optional


app = FastAPI()

hello = []


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return {"hello": hello, "limit": limit}


@app.get("/items")
async def read_items(item_id: int):
    return {"item_id": item_id}


@app.get("/items")
async def read_items(item_id: int, q: str | None = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items")
async def read_items(item_id: int, price: float):
    return {"item_id": item_id, "price": price}


@app.get("/items")
async def read_items(item_id: int, is_available: bool = True):
    return {"item_id": item_id, "is_available": is_available}
