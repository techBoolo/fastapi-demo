from fastapi import FastAPI

app = FastAPI()


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


@app.get("/users/{user_id}")
async def show_user(user_id):
    return {"message": "list of users", "id": user_id }


