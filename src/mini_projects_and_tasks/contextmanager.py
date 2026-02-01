from fastapi import FastAPI
import time
from contextlib import asynccontextmanager
import logging
import os

log = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app : FastAPI):
    try:
        app.state.request_count = 0
        log.ingo("Request counter initialized")
        yield
    finally:
        log.info(f"Total requests: {app.state.request_count}")
        app.state.request_count = 0

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def hello():
    app.state.request_count += 1
    return {"message": "Hello, World!"}