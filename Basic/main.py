# from fastapi import FastAPI

# app=FastAPI()

# @app.get('/student')
# def get():
#     return {
#         'name':'krishna',
#             'rollno':41,
#             'age':24
#         }

#path parameter
# @app.get('/student/{name}/{student_id}')
# def get_student(name:str,student_id:int):
#     return {
#         'name':name,
#         'student_id':student_id
#         }

# #Quary parameter
# @app.get('/student/')    #http://127.0.0.1:8000/student/?age=26&city=parola
# def get(age:int, city:str='pune'):
#     return {
#         "age":age,
#         "city":city
#     }

#CRUD operation simple without fectch data in database
# from fastapi import FastAPI
# from pydantic import BaseModel

# app=FastAPI()

# class Student(BaseModel):
#     name:str 
#     rollno:int 
#     marks:float

# #psot
# @app.post('/student/')
# def create_student(student:Student):
#     return {
#         'msg':'student created successfully.',
#         'student':student
#     }

# @app.get('/student/')
# def get_student(student:Student):
#     return student

# #put
# @app.put('/student/{id}')
# def update_student(id:int,student:Student):
#     return {
#         'mgs':'student update successfully..',
#         'rollno':id,
#         'update_data':student
#     }

# # #delete
# @app.delete('/student/{id}')
# def delete_student(id:int):
#     return {
#         "msg":"student deleted successfully..",
#         "id":id
#     }
# students=[]
# #student by id
# @app.get("/student/{id}")
# def get_by_id(id: int):
#     for stu in students:
#         if stu.id == id:
#             return stu
#         else:
#             return{'msg':'student not meet.'}

#Response Models
# from fastapi import FastAPI
# from pydantic import BaseModel

# app=FastAPI()

# class Student(BaseModel):
#     name:str 
#     rollno:int
#     marks:float

# class StudentResponse(BaseModel):
#     name:str 
#     marks:float

# @app.get('/student/',response_model=StudentResponse)
# def stu_resp():
#     return {
#         'name':'swami',
#         'rollno':46,
#         'marks':89.90
#     }

#Dependency injection
from fastapi import FastAPI,Depends


app=FastAPI()

students = [
    {"name": "Swapnil", "rollno": 41, "marks": 85.5},
    {"name": "Rahul", "rollno": 42, "marks": 78.0}
]

@app.get('/students/')
def get_student():
    return students

@app.get('/students/')
def get(data=Depends(get_student)):
    return data

@app.get('/students/')
def student_count(data=Depends(get_student)):
    return {"total_student":len(data)}


