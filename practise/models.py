from sqlalchemy import Column,String,Integer,Float
from database import Base

class Product(Base):
    __tablename__='product'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    qty=Column(Integer,unique=True,nullable=False)
    price=Column(Float,nullable=False)
    quality=Column(String,nullable=False)


