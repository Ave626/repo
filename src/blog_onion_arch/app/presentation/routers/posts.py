from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.application.services.post_service import PostService
from app.application.schemas.post import PostRead, PostBase
from app.presentation.dependencies import get_post_service

router = APIRouter()


@router.post("/", response_model=PostRead, status_code=201)
async def create_post_endpoint(
        post_data: PostBase,
        service: PostService = Depends(get_post_service)
):
    try:
        return await service.create_post(post_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{post_id}", response_model=PostRead)
async def read_post_endpoint(
        post_id: int,
        service: PostService = Depends(get_post_service)
):
    db_post = await service.get_post_id(post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.get("/", response_model=List[PostRead])
async def read_posts_endpoint(
        skip: int = 0, limit: int = 100,
        service: PostService = Depends(get_post_service)
):
    posts = await service.get_all_posts(skip=skip, limit=limit)
    return posts


@router.get("/category/{category_id}", response_model=List[PostRead])
async def read_posts_by_category_endpoint(
        category_id: int, skip: int = 0, limit: int = 100,
        service: PostService = Depends(get_post_service)
):
    posts = await service.get_posts_by_category_id(category_id, skip=skip, limit=limit)
    return posts
