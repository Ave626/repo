from fastapi import APIRouter,Depends,Heade,HTTPException,status
from typing import List
from app.core.dependencies import get_category_service
from app.schemas.category import Category,CategoryBase
from app.services.categories import CategoryService

router = APIRouter(prefix="/categories",tags=["categories"])

@router.get("/",response_model=List[Category])
async def read_categories(skip : int = 0,limit : int = 0,category_service : CategoryService = Depends(get_category_service)):
    categories = await category_service.get_all_categories(skip=skip,limit=limit)
    return categories

@router.post("/",response_model=Category,status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryBase, category_service : CategoryService = Depends(get_category_service)):
    db_category = await category_service.create_category(category=category)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Категория с таким именем уже существует")
    return db_category

@router.get("/{category_id}",response_model=Category)
async def read_category(category_id : int,category_service: CategoryService = Depends(get_category_service)):
    db_category = await category_service.get_category_by_id(category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404,detail="Категория не найдена")
    return db_category

