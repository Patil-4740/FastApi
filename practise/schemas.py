from pydantic import BaseModel

class ProductCreate(BaseModel):
    name:str 
    qty:int 
    price:float
    quality:str

    


