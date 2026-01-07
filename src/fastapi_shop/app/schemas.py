from pydantic import BaseModel,Field,ConfigDict,EmailStr
from datetime import datetime
from decimal import Decimal

class CategoryCreate(BaseModel):
    name: str = Field(...,min_length=3,max_length=50,description="Назвнаие категории")
    parent_id: int | None = Field(None,description="ID родительской категории")

class Category(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор")
    name: str = Field(..., description="Название категории")
    parent_id: int | None = Field(None, description="ID родительской категории, если есть")
    is_active: bool = Field(..., description="Активность категории") 
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100,description="Название товара (3-100 символов)")
    description: str | None = Field(None, max_length=500,description="Описание товара (до 500 символов)")
    price: Decimal = Field(..., gt=0, description="Цена товара (больше 0)", decimal_places=2)
    image_url: str | None = Field(None, max_length=200, description="URL изображения товара")
    stock: int = Field(..., ge=0, description="Количество товара на складе (0 или больше)")
    category_id: int = Field(..., description="ID категории, к которой относится товар")

class Product(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор товара")
    name: str = Field(..., description="Название товара")
    description: str | None = Field(None, description="Описание товара")
    price: Decimal = Field(..., description="Цена товара в рублях", gt=0, decimal_places=2)
    image_url: str | None = Field(None, description="URL изображения товара")
    stock: int = Field(..., description="Количество товара на складе")
    category_id: int = Field(..., description="ID категории")
    is_active: bool = Field(..., description="Активность товара")
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email: EmailStr = Field(description="Email пользователя")
    password: str = Field(min_length=8,description="Пароль(минимум 8 символов)")
    role: str = Field(default="buyer",pattern="^(buyer|seller)$",description="Роль: 'buyer' или 'seller'")

class User(BaseModel):
    id : int = Field(...,description="ID пользователя")
    email : EmailStr = Field(...,description="Почта пользователя")
    is_active : bool = Field(...,description="Активность пользователя")
    role : str = Field(...,description="Роль пользователя")
    model_config = ConfigDict(from_attributes=True)

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class Review(BaseModel):
    id : int = Field(...,description="Уникальный идентификатор отзыва")
    user_id : int = Field(...,description="ID пользователя")
    product_id : int = Field(...,description="ID продукта")
    comment : str | None = Field(...,description="Текст комментария")
    comment_date : datetime = Field(...,description="Дата комментария")
    grade : int = Field(...,description="Оценка от 1 до 5")    
    is_active: bool = Field(True, description="Активность отзыва")

class ReviewCreate(BaseModel):
    product_id : int = Field(...,description="ID продукта")
    comment : str | None = Field(...,description="Текст комментария")
    grade : int = Field(...,ge=1,le=5,description="Оценка от 1 до 5")