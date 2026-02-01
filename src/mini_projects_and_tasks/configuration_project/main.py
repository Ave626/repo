from fastapi import FastAPI,Depends
from config import Settings,get_settings

app = FastAPI()
@app.get("/settings")
async def get_api_settings(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "database_url": settings.database_url,
        "secret_key_snippet": settings.secret_key[:8] + "..." # Обрезаем секретный ключ для безопасности
    }