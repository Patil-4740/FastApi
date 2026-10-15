from fastapi import FastAPI
from database import Base,engine, SessionLocal
from models import Student
from schemas import StudentCreate,StudentUpdate


app=FastAPI()

Base.metadata.create_all(bind=engine)

#show all
@app.get('/student/')
def get_stu():
    db=SessionLocal()
 
    student=db.query(Student).all()

    db.close()
    return student

#post data
@app.post('/student/')
def put_stu(student:StudentCreate):
    db=SessionLocal()

    new_student=Student(
        name=student.name,
        age=student.age,
        email=student.email,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    return{
        'msg':'student created successfully..',
        'id':new_student.id,
        'name':new_student.name,
        'age':new_student.age,
        'email':new_student.email,
        'marks':new_student.marks
    }

@app.get('/student/{id:int}')
def getById_stu(id:int):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'student not found'}
    else:
        return student

@app.delete('/student/{id:int}')
def delete_stu(id:int):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'Student not found..'}
    db.delete(student)
    db.commit()

    return {'msg':'Student Deleted successfully..'}

@app.put('/student/{id}')
def put_stu(id:int,student_put:StudentCreate):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'student not found..'}

    student.name=student_put.name
    student.age=student_put.age
    student.email=student_put.email 
    student.marks=student_put.marks

    db.commit()
    db.refresh(student)

    return {
        'msg':'student updated successfully.',
        'id':student.id,
        'name':student.name,
        'age':student.age,
        'email':student.email,
        'marks':student.marks
    }

@app.patch('/student/{id:int}')
def patch_stu(id:int,student_patch:StudentUpdate):
    db=SessionLocal()

    student=db.query(Student).filter(Student.id==id).first()

    if student is None:
        return {'msg':'student not found..'}

    upated_student=student_patch.model_dump(exclude_unset=True)
    for key,value in upated_student.items():
        setattr(student,key,value)

    db.commit()
    db.refresh(student)

    return {
        'msg':'Student updated successfuly.',
        'id':student.id,
        'name':student.name,
        'age':student.age,
        'email':student.email,
        'marks':student.marks
    }

