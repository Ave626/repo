from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis

@asynccontextmanager
async def lifespan(app : FastAPI):
    redis_connection = redis.from_url("redis://localhost",encoding="utf-8",decode_responses=True)
    await FastAPILimiter.init(redis_connection)
    print("FastAPI Limiter инициализорован с Redis")

    yield
    await redis_connection.close()
    print("Соединение c Redis закрыто.")

app = FastAPI(lifespan=lifespan)

@app.get("/info",dependencies=[Depends(RateLimiter(times=5,minutes=5))])
async def get_info():
    return {"message": "Это защищенная информация"}
