from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import select,update
from sqlalchemy.ext.asyncio import AsyncSession
from app.db_depends import get_async_db
from app.models.reviews import Review as ReviewModel
from app.models.users import User as UserModel
from app.models.products import Product as ProductModel
from app.schemas import Review as ReviewSchema,ReviewCreate
from app.auth import get_current_seller,get_current_admin,get_current_buyer
from sqlalchemy.sql import func

router = APIRouter(prefix="/reviews",tags=["reviews"])


async def update_product_rating(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(func.avg(ReviewModel.grade)).where(
            ReviewModel.product_id == product_id, 
            ReviewModel.is_active == True
        )
    )
    avg_rating = result.scalar() or 0.0
    await db.execute(
        update(ProductModel)
        .where(ProductModel.id == product_id)
        .values(rating=float(avg_rating))
    )
    await db.commit()

@router.get("/",response_model = list[ReviewSchema],status_code=status.HTTP_200_OK)
async def get_all_reviews(db : AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(ReviewModel).where(ReviewModel.is_active == True))
    return result.all()

@router.post("/",response_model=ReviewSchema,status_code=status.HTTP_201_CREATED)
async def create_the_review(review : ReviewCreate,db : AsyncSession = Depends(get_async_db),current_user : UserModel = Depends(get_current_buyer)):
    result_product = await db.scalars(select(ProductModel).where(ProductModel.id == review.product_id,ProductModel.is_active == True))
    product = result_product.first()
    if product is None:
        raise HTTPException(status_code=404,detail="Товар не найден или не активен")
    if product.seller_id == current_user.id:
        raise HTTPException(status_code=403, detail="Вы не авторизированы")
    db_review = ReviewModel(**review.model_dump(),user_id = current_user.id)
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    await update_product_rating(db,product.id)
    return db_review

@router.delete("/{review_id}",status_code=status.HTTP_200_OK)
async def delete_the_review(review_id : int,db : AsyncSession = Depends(get_async_db),current_user : UserModel = Depends(get_current_admin)):
    result_review = await db.scalars(select(ReviewModel).where(ReviewModel.id == review_id,ReviewModel.is_active == True))
    review = result_review.first()
    if review is None:
        raise HTTPException(status_code=404,detail="Отзыв не найден или не активен")
    await db.execute(update(ReviewModel).where(ReviewModel.id == review_id,ReviewModel.is_active == True).values(is_active=False))
    await db.commit()
    await update_product_rating(db,review.product_id)
    return {"message": "Review deleted"}
