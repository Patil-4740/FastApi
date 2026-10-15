from fastapi import FastAPI
from database import engine,Base,SessionLocal
from models import Product
from schemas import ProductCreate

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/product/')
def get_pro():
    db=SessionLocal()

    product=db.query(Product).all()
    db.close()
    return product

@app.post('/product/')
def post_pro(product:ProductCreate):
    db=SessionLocal()

    new_product=Product(
        name=product.name,
        qty=product.qty,
        price=product.price,
        quality=product.quality
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return {
        'msg':'product created successfully.',
        'id':new_product.id,
        'name':new_product.name,
        'qty':new_product.qty,
        'price':new_product.price,
        'quality':new_product.quality
    }

@app.get('/product/{id}')
def getById(id:int):
    db=SessionLocal()

    product=db.query(Product).filter(Product.id==id).first()
    if product is None:
        return{'msg':'product not found..'}
    else:
        return product

@app.delete('/product/{id}')
def delete_pro(id:int):
    db=SessionLocal()

    product=db.query(Product).filter(Product.id==id).first()

    if product is None:
        return{'msg':'Product not found..'}
    db.delete(product)
    db.commit()

    return{'msg':"Product deleted successfully.."}

@app.put('/product/{id}')
def put_pro(id:int,product_data:ProductCreate):
    db=SessionLocal()

    product=db.query(Product).filter(Product.id==id).first()

    if product is None:
        return{'msg':'product not found..'}

    product.nane=product_data.name
    product.qty=product_data.qty 
    product.price=product_data.price
    product.quality=product_data.quality

    db.commit()
    db.refresh(product)

    return {
        'msg':'Product updated successfully..',
        'id':product.id,
        'name':product.name,
        'qty':product.qty,
        'price':product.qty,
        'quality':product.quality
    }


@app.patch('/product/{id}')
def patch_pro(id:int,product_data:ProductCreate):
    db=SessionLocal()

    product=db.query(Product).filter(Product.id==id).first()

    if product is None:
        return {"msg":"Product Not found.."}

    update_data=product_data.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(product,key,value)

    db.commit()
    db.refresh(product)

    return{
        'msg':'Product update successfully..',
        'id':product.id,
        'name':product.name,
        'aty':product.qty,
        'price':product.price,
        'quality':product.quality
    }

