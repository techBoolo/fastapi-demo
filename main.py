from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Gender(str, Enum):
    maler = "Male",
    female = "Female"


@app.on_event(event_type="startup")
async def startup():
    print("app started")


@app.on_event("shutdown")
async def shutdown_event():
    print("app shutdown")


@app.get("/")
async def root():
    return {"message": "root route"}


@app.get("/users")
async def index_users():
    return {"message": "list of users"}

@app.get("/users/gender/{gender}")
async def index_users_gender(gender: Gender):
    return {"message": "list of users", "gender": gender }


@app.get("/users/{user_id}")
async def show_user(user_id):
    return {"message": "user detail", "id": user_id }


@app.get("/posts/latest")
async def get_latest():
    return { "message": "latest posts" }


@app.get("/posts/{post_id}")
async def show_post(post_id: int):
    return {"message": "post detail", "id": post_id }

