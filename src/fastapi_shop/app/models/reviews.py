from sqlalchemy import Boolean,String,ForeignKey
from app.database import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Integer,String,ForeignKey,Text,DateTime,Boolean,CheckConstraint,UniqueConstraint
from datetime import datetime

class Review(Base):
    __tablename__ = "reviews"
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id"))
    comment : Mapped[str] = mapped_column(Text,nullable = True)
    comment_date : Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    grade: Mapped[int] = mapped_column(Integer, CheckConstraint("grade >= 1 AND grade <= 5"), nullable=False)
    is_active : Mapped[bool] = mapped_column(Boolean,default=True)
    product : Mapped["Product"] = relationship("Product",back_populates="reviews")
    user : Mapped["User"] = relationship("User",back_populates="reviews")
    __table_args__ = (UniqueConstraint("user_id", "product_id", name="uq_user_product_review"),)

