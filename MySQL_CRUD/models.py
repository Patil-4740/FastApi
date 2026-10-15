from sqlalchemy import Column,String,Integer,Float
from database import Base

class Student(Base):

    __tablename__='student'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    age=Column(Integer,nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    marks=Column(Float,nullable=False)

    