from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Boolean,Integer,String
from app.database import Base
from typing import List

class User(Base):
    __tablename__= "users"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    email : Mapped[str] = mapped_column(String,unique=True,index=True,nullable=False)
    hashed_password : Mapped[str] = mapped_column(String,nullable = False)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True)
    role : Mapped[str] = mapped_column(String,default="buyer")
    products : Mapped[list["Product"]] = relationship("Product",back_populates="seller")
    reviews : Mapped[List["Review"]] = relationship("Review",back_populates="user")
    cart_items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="user")
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")