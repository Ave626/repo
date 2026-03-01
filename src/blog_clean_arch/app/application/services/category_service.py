from typing import List
from app.domain.models.category import Category
from app.domain.repositories.categories import ICategoryRepository
from app.application.schemas.category import CategoryCreate

class CategoryService:
    def __init__(self,category_repo : ICategoryRepository):
        self.category_repo = category_repo

    async def get_category_by_id(self,category_id : int) -> Category | None:
        return await self.category_repo.get_by_id(category_id)
    
    async def get_category_by_name(self,name : str) -> Category | None:
        return await self.category_repo.get_by_name(name)
    
    async def get_all_categories(self,skip : int = 100,limit : int = 100) -> List[Category]:
        return await self.category_repo.get_all(skip,limit)
    
    async def create_category(self,category_data : CategoryCreate) -> Category:
        existing_category = await self.category_repo.get_by_name(category_data.name)
        if existing_category:
            raise ValueError(f"Категория с именем '{category_data.name}'уже существует")
        new_category = Category(name=category_data.name)
        return await self.category_repo.create(new_category)