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
async def index_users(page: int = 1, size: int = 10, q: str | None = None):
    response = {"message": "list of users"}
    response.update({"page": page})
    response.update({"size": size})
    if q:
        response.update({"q": q})
    return response


@app.get("/users/gender/{gender}")
async def index_users_gender(gender: Gender):
    return {"message": "list of users", "gender": gender}


@app.get("/users/{user_id}")
async def show_user(user_id, q: str | None = None):
    response = {"message": "user detail", "id": user_id}
    if q:
        response.update({"q": q})
    return response


@app.get("/posts")
async def get_posts(q: str | None = None, short: bool = False):
    response = {"message": "list of posts"}
    if q:
        response.update({"q": q})
    if not short:
        response.update({"description": "this post is long and requires some "
                                        "time to read"})
    return response


@app.get("/posts/latest")
async def get_latest(sort: str):
    return {"message": "latest posts"}


@app.get("/posts/{post_id}")
async def show_post(post_id: int):
    return {"message": "post detail", "id": post_id}
