from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app import schemas
from app.database import get_async_db
from app.models.category import Category
router = APIRouter(prefix="/categories",tags=["categories"])

@router.get("/",response_model=List[schemas.Category])
async def read_categories(skip: int = 0,limit : int = 100,db : AsyncSession = Depends(get_async_db)):
    categories = await db.scalars(select(Category).offset(skip).limit(limit))
    return categories.all()

@router.post("/",response_model=schemas.Category,status_code=201)
async def create_category(category : schemas.CategoryBase,db : AsyncSession = Depends(get_async_db)):
    db_category = await db.scalars(select(Category).filter(Category.name == category.name))
    if db_category.first():
        raise HTTPException(status_code=400, detail="Категория с таким именем уже существует")
    db_category = Category(name = category.name)
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

@router.get("/{category_id}",response_model=schemas.Category)
async def read_category(category_id : int,db : AsyncSession = Depends(get_async_db)):
    db_category = await db.scalars(select(Category).filter(Category.id == category_id))
    if db.category.first() is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category