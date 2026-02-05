from sqlalchemy import String,Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.infrastructure.database.connection import Base

class Post(Base):
    __tablename__="posts"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[str] = mapped_column(String,index=True)
    content : Mapped[str] = mapped_column(String)
    category_id : Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"))
    category : Mapped["Category"] = relationship("Category", back_populates="posts")
