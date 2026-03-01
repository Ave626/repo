from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.infrastructure.database.connection import create_db_and_tables
from app.presentation.routers import categories,posts

@asynccontextmanager
async def lifespan(app : FastAPI):
    print("Приложение запускается")
    await create_db_and_tables()
    print("База данных инициализирована")
    yield
    print("Приложение завершило работу")

app = FastAPI(title="Clean_blog_arch",lifespan=lifespan)

app.include_router(categories.router)
app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message" : "Initial message"}