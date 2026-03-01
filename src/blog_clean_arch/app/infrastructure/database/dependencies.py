from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import AsyncGenerator
from app.domain.repositories.categories import ICategoryRepository
from app.domain.repositories.posts import IPostRepository
from app.infrastructure.persistence.sqlalchemy.category_repository import SQLAlchemyCategoryRepository
from app.infrastructure.persistence.sqlalchemy.posts_repository import SQLAlchemyPostRepository
from app.application.services.category_service import CategoryService
from app.application.services.post_service import PostService
from app.infrastructure.database.connection import AsyncSessionLocal

async def get_db_session() -> AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal() as session:
        yield session

def get_category_repository_impl(db_session : AsyncSession = Depends(get_db_session)) -> ICategoryRepository:
    return SQLAlchemyCategoryRepository(db_session)

def get_post_repository_impl(db_session : AsyncSession = Depends(get_db_session)) -> IPostRepository:
    return SQLAlchemyPostRepository(db_session)

def get_category_service_impl(category_repo : ICategoryRepository = Depends(get_category_repository_impl)) -> CategoryService:
    return CategoryService(category_repo=category_repo)

def get_post_service_impl(post_repo: IPostRepository = Depends(get_post_repository_impl),category_repo: ICategoryRepository = Depends(get_category_repository_impl)) -> PostService:
    return PostService(post_repo=post_repo, category_repo=category_repo)
