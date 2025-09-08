from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index(name: str, price: int):
    print(name, price)
    return {"name": name, "price": price}