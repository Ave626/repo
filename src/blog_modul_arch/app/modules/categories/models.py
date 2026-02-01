from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    name : Mapped[str] = mapped_column(String,unique=True)
    posts : Mapped[list["Post"]] = relationship("Post",back_populates="category")