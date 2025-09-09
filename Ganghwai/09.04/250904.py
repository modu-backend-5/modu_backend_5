from fastapi import FastAPI

app = FastAPI()


@app.get("/users") # 127.0.0.1:8000/users
def get_users():

    return {
        "user1": {"name": "max", "password": 1234},
        "user2": {"name": "good", "password": 1111},
    }


@app.get("/")
def read_root():

    return {"Hello": "World"}

@app.get("/about")
def about():

    return {"message": "About page"}

@app.get("/contact")
def contact():

    return {"message": "Contact page"}

@app.get("/notice")
def notice():

    return {"notices": ["공지사항1": {"헬로헬로"}
                        "공지사항2": {"굿모닝굿모닝"}
    ]}