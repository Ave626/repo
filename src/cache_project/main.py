import json
import time
from typing import Dict,Optional
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
import redis.asyncio as redis
from contextlib import asynccontextmanager

redis_client : Optional[redis.Redis] = None

class Item(BaseModel):
    id : str
    name : str
    value : int

fake_database: Dict[str,Item] = {}

@asynccontextmanager
async def lifespan(app : FastAPI):
    print("Запуск приложения")
    global redis_client
    global fake_database
    redis_client = redis.Redis(host='localhost',port=6379,db=0,decode_responses=True)
    try:
        await redis_client.ping()
        print("Успешно подключено к Redis")
    except redis.ConnectionError as e:
        print(f"Не удалось подклюиться к Redis:{e}")
        redis_client = None
    fake_database["item:1"] = Item(id="1", name="Продукт A", value=10)
    fake_database["item:2"] = Item(id="2", name="Продукт B", value=20)
    print("Фейковая база данных инициализирована данными.")

    yield

    print("Завершение работы приложения")
    if redis_client:
        await redis_client.close()
        print("Отключено от Redis")

app = FastAPI(lifespan=lifespan)

async def get_redis_client_dependency():
    if redis_client is None:
        raise HTTPException(status_code=500,detail="Клиент Redis не инициализирован или не подключен.")
    return redis_client

@app.get('/redis_connect')
async def redis_connect_test(r: redis.Redis = Depends(get_redis_client_dependency)):
    await r.ping()
    return {'message': 'Успешное подключение к Redis'}


@app.get("/itme/{item_id}",response_model=Item)
async def get_item(item_id : str,r : redis.Redis = Depends(get_redis_client_dependency)):
    cache_key = f"item:{item_id}"
    cached = await r.get(cache_key)
    if cached:
        data = json.loads(cached)
        item = Item.model_validate(data)
        return item
    item = fake_database.get(item_id)
    time.sleep(2)
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    await r.set(cache_key,json.dumps(item.model_dump()),ex=60)
    return item

@app.post("/item", response_model=Item)
async def create_item(item: Item, r: redis.Redis = Depends(get_redis_client_dependency)):
    fake_database[item.id] = item
    cache_key = f"item:{item.id}"
    await r.delete(cache_key)
    return item