from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routers import categories,posts
from app.core.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app : FastAPI):
    print("Приложение заупскается")
    await create_db_and_tables()
    print("База данных инициализирована.")
    yield
    print("Приложение завершает работу.")

app = FastAPI(title="Многоуровневая архитектура",lifespan=lifespan)

app.include_router(categories.router)
app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Эндпоинт для проверки"}