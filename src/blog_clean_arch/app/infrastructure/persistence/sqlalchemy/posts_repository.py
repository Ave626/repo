from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.models.post import Post
from app.domain.repositories.posts import IPostRepository
from app.infrastructure.persistence.sqlalchemy.models import PostORM

class SQLAlchemyPostRepository(IPostRepository):
    def __init__(self,db_session: AsyncSession):
        self.db_session = db_session

    def _to_domain_model(self, orm_model: PostORM) -> Post:
        return Post(
            id=orm_model.id,
            title=orm_model.title,
            content=orm_model.content,
            category_id=orm_model.category_id
        )

    def _to_orm_model(self, domain_model: Post) -> PostORM:
        return PostORM(
            id=domain_model.id,
            title=domain_model.title,
            content=domain_model.content,
        )
    
    async def get_by_id(self,post_id : int) -> Post | None:
        orm_post = await self.db_session.scalar(select(PostORM).where(PostORM.id == post_id))
        if orm_post is None:
            return None
        return self._to_domain_model(orm_post)
    
    async def get_by_category_id(self,category_id : int,skip : int = 0,limit : int = 100) -> List[Post]:
        result = await self.db_session.scalars(select(PostORM).where(PostORM.category_id == category_id))
        orm_posts = list(result.all())
        return[self._to_domain_model(post) for post in orm_posts]
    
    async def get_all(self,skip : int = 0,limit : int = 100) -> List[Post]:
        result = await self.db_session.scalars(select(PostORM).offset(skip).limit(limit))
        orm_posts = list(result.all())
        return [self._to_domain_model(post) for post in orm_posts]
    
    async def create(self,post : Post) -> Post:
        db_post_orm = self._to_orm_model(post)
        self.db_session.add(db_post_orm)
        await self.db_session.commit()
        await self.db_session.refresh(db_post_orm, attribute_names=["category_rel"])
        return self._to_domain_model(db_post_orm)

