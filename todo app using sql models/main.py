from fastapi import FastAPI
from database import init_db
from routers import admin, user, task

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(admin.router)
app.include_router(user.router)
