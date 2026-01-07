from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update
from app.models.products import Product as ProductModel
from app.models.categories import Category as CategoryModel
from app.models.reviews import Review as ReviewModel
from app.schemas import Product as ProductSchema, ProductCreate,Review as ReviewSchema,ReviewCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.db_depends import get_async_db
from app.models.users import User as UserModel
from app.auth import get_current_seller


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductSchema])
async def get_all_products(db: AsyncSession = Depends(get_async_db)):
    stmt = select(ProductModel).where(ProductModel.is_active == True)
    products = await db.scalars(stmt)
    result = products.all()    
    return result


@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate,db: AsyncSession = Depends(get_async_db),current_user: UserModel = Depends(get_current_seller)):
    category_result = await db.scalars(select(CategoryModel).where(CategoryModel.id == product.category_id, CategoryModel.is_active == True))
    if not category_result.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Категория не найдена или не активна")
    db_product = ProductModel(**product.model_dump(), seller_id=current_user.id)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)  
    return db_product



@router.get("/category/{category_id}", response_model=list[ProductSchema])
async def get_products_by_category(category_id: int, db: AsyncSession = Depends(get_async_db)):
    stmt = await db.scalars(select(CategoryModel).where(CategoryModel.id == category_id,CategoryModel.is_active == True))
    category = stmt.first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Категория не найдена или не активна")
    stmt_products = await db.scalars(select(ProductModel).where(ProductModel.category_id == category_id,ProductModel.is_active == True))
    products = stmt_products.all()
    return products


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product(product_id: int, db: AsyncSession = Depends(get_async_db)):
    stmt = await db.scalars(select(ProductModel).where(ProductModel.id == product_id, ProductModel.is_active == True))
    product = stmt.first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Товар не найден или не активен")
    return product

@router.put("/{product_id}", response_model=ProductSchema)
async def update_product(product_id: int,product: ProductCreate,db: AsyncSession = Depends(get_async_db),current_user: UserModel = Depends(get_current_seller)):
    result = await db.scalars(select(ProductModel).where(ProductModel.id == product_id, ProductModel.is_active == True))
    db_product = result.first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товар не найден или не активен")
    if db_product.seller_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вы можете изменять только свои товары")
    category_result = await db.scalars(select(CategoryModel).where(CategoryModel.id == product.category_id, CategoryModel.is_active == True))
    if not category_result.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Категория не найдена или не активна")
    await db.execute(update(ProductModel).where(ProductModel.id == product_id).values(**product.model_dump()))
    await db.commit()
    await db.refresh(db_product)  
    return db_product



@router.delete("/{product_id}", response_model=ProductSchema)
async def delete_product(product_id: int,db: AsyncSession = Depends(get_async_db),current_user: UserModel = Depends(get_current_seller)):
    result = await db.scalars(select(ProductModel).where(ProductModel.id == product_id, ProductModel.is_active == True))
    product = result.first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Товар не найден или не активен")
    if product.seller_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Вы можете менять только свои товары")
    await db.execute(update(ProductModel).where(ProductModel.id == product_id).values(is_active=False))
    await db.commit()
    await db.refresh(product)
    return product

@router.get("/{product_id}/reviews/",response_model=list[ReviewSchema],status_code=status.HTTP_200_OK)
async def get_all_reviews_by_product(product_id : int,db : AsyncSession = Depends(get_async_db)):
    result = await db.scalars(select(ProductModel).where(ProductModel.id == product_id,ProductModel.is_active == True))
    product = result.first()
    if product is None:
        raise HTTPException(status_code=404,detail="Товар не существует или не активен")
    result_review = await db.scalars(select(ReviewModel).where(ReviewModel.product_id == product.id))
    reviews = result_review.all()
    return reviews