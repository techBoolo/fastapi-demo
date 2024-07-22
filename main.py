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
