from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import relationship,mapped_column,Mapped
from app.core.database import Base

class Post(Base):
    __tablename__ = "posts"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[str] = mapped_column(String,index=True)
    content : Mapped[str] = mapped_column(String)
    category_id : Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"))
    category : Mapped["Category"] = relationship("Category",back_populates="posts")
    