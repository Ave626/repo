from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column

from app.database import Base

class Post(Base):
    __tablename__="posts"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    title : Mapped[str] = mapped_column(String,index=True)
    content : Mapped[str] = mapped_column(String)
    category_id : Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"))
    category : Mapped["Category"] = relationship("Category",back_populates="posts")
    

