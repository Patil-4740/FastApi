from fastapi import FastAPI
from database import engine,Base, SessionLocal
from models import Student
from schemas import StudentCreate

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/student/')
def show_stu():
    db=SessionLocal()

    student=db.query(Student).all()
    db.close()
    return student

#GetBy Id data
@app.get('/student/{id}')
def put_stu(id:int):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first() #first means return the matching data 
    db.close()
    if student is None:
        return {'msg':'student not found'}
    else:
        return student

# #Delete Data
@app.delete('/student/{id}')
def delete_stu(id:int):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()
    
    if student is None:
        return {'msg':'Student not found..'}
    db.delete(student)
    db.commit()

    return {'msg':'student deleted successfully..'}


#Put Data
@app.put('/student/{id}')
def put_stu(id:int,student_data:StudentCreate):

    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'Student not found...'}

    student.name=student_data.name
    student.rollno=student_data.rollno
    student.marks=student_data.marks

    db.commit()
    db.refresh(student)

    return{
        'msg':'Student updated succssfully..',
        'id':student.id,
        'name':student.name,
        'rollno':student.rollno,
        'marks':student.marks
    } 

@app.patch('/student/{id}')
def patch_stu(id:int,student_data:StudentCreate):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'Student not found'}

    update_data=student_data.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(student,key,value)

    db.commit()
    db.refresh(student)

    return {
        'msg':'Student update successfully..',
        'id':student.id,
        'name':student.name,
        'rollno':student.rollno,
        'marks':student.marks
    }
 
