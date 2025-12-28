import os
import sys
from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))  
from app.database import Base
from typing import List
class Category(Base):
    __tablename__ = "categories"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)
    parent_id : Mapped[str] = mapped_column(ForeignKey("categories.id"),nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True) 
    products : Mapped[List["Product"]] = relationship("Product",back_populates="category")
    parent : Mapped["Category | None"] = relationship("Category",back_populates="children",remote_side="Category.id")
    children: Mapped[List["Category"]] = relationship("Category",back_populates="parent")
