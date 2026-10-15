from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    age:int
    email:str
    marks:float 

class StudentUpdate(BaseModel):
    name:str | None=None
    age:int  | None=None
    email:str| None=None
    marks:float| None=None

