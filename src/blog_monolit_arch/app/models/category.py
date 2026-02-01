from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship,Mapped,mapped_column

from app.database import Base

class Category(Base):
    __tablename__ = "categories"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String,unique=True)
    posts : Mapped[list["Post"]] = relationship("Post",back_populates="category")