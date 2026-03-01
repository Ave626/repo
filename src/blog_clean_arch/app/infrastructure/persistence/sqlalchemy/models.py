from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped
from app.infrastructure.database.connection import Base

class CategoryORM(Base):
    __tablename__ = "categories"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String,unique=True)
    posts : Mapped[list["PostORM"]] = relationship("PostORM",back_populates="category_rel")
    def __repr__(self):
        return f"<CategoryORM(id={self.id}, name='{self.name}')>"

class PostORM(Base):
    __tablename__="posts"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[str] = mapped_column(String,index=True)
    content : Mapped[str] = mapped_column(String)
    category_id : Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"))
    category_rel : Mapped["CategoryORM"] = relationship("CategoryORM",back_populates="posts")
    