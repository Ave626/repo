from fastapi import FastAPI, Request
from slowapi import Limiter,_rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)

@app.get("/home")
@limiter.limit("5/minute")
async def homepage(request : Request):
    return {'message': 'Главная страница'}

@app.get("/profile")
@limiter.limit("10/hour") 
async def profile_page(request: Request):
    return {"message": "Это ваш профиль."}

@app.get("/unlimited")
async def unlimited_page(request: Request):
    return {"message": "Эта страница без ограничений."}