from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app import schemas
from app.database import get_async_db
from app.models.category import Category
from app.models.post import Post

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.get("/", response_model=List[schemas.Post])
async def read_posts(category_id: int | None = None, skip: int = 0, limit: int = 100,db: AsyncSession = Depends(get_async_db)):
    query = select(Post)
    if category_id is not None:
        category = await db.scalar(select(Category).filter(Category.id == category_id))
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        query = query.filter(Post.category_id == category_id)
    posts = await db.scalars(query.offset(skip).limit(limit))
    return posts.all()

@router.post("/", response_model=schemas.Post, status_code=201)
async def create_post(post: schemas.PostBase, db: AsyncSession = Depends(get_async_db)):
    category = await db.scalar(select(Category).filter(Category.id == post.category_id))
    if category is None:
        raise HTTPException(status_code=400, detail="Invalid category_id")

    db_post = Post(
        title=post.title,
        content=post.content,
        category_id=post.category_id
    )
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

@router.get("/{post_id}", response_model=schemas.Post)
async def read_post(post_id: int, db: AsyncSession = Depends(get_async_db)):
    db_post = await db.scalar(select(Post).filter(Post.id == post_id))
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
