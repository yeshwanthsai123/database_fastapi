from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import models as s
from    models import Student,StudentGrade,parentdetails
from database import engine, SessionLocal, Base
from schemas import mobgrade,emailgrade
Base.metadata.create_all(bind=engine)
 
app = FastAPI()
 
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management API"}


@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = s.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
 
@app.get("/students")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(s.Student).filter(s.Student.student_id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
 
@app.post("/grades/")
def create_grade(grade: schemas.StudentGradeCreate, db: Session = Depends(get_db)):
    # return crud.create_student_grade(db, grade)
    student = db.query(s.Student).filter(s.Student.student_id==grade.student_id).first()
    if student:
        student_grade = s.StudentGrade(student_garde_in_c = grade.student_grade_in_c,
                                            student_grade_in_python = grade.student_grade_in_python,
                                            student_grade_in_java = grade.student_grade_in_java,
                                            student_id = grade.student_id)
        db.add(student_grade)
        db.commit()
        db.refresh(student_grade)
        return student_grade
    return {"message": "Student not present"}
    # return grade
    # db_grade = models.StudentGrade(**grade.dict())
    # db.add(db_grade)
    # db.commit()
    # db.refresh(db_grade)
    # return db_grade
 
@app.get("/students/")
def read_all_students(db: Session = Depends(get_db)):
    return db.query(s.Student).all()
 
@app.put("/update_student/")
def update(student_id: int, mobile_number : int=None, email: str=None ,db:Session=Depends(get_db)):
    student = db.query(Student).filter(Student.student_id==student_id).first()
    if student:
        if mobile_number:
            student.student_mobile_number = mobile_number
        if email:
            student.student_email_id = email
        db.commit()
        db.refresh(student)
        return student
    return {"Message":"Student Not exists"}
 
@app.delete("/deletedata")
def delete(student_id: int, db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.student_id==student_id).first()
    if student:
     db.delete(student)
     db.commit()
     return student
    return{"message":"no"}
   
@app.get("/providegrade")
def number(mob:int,db:Session=Depends(get_db)):
    Student_mob=db.query(Student).filter(Student.student_mobile_number==mob).first()
    if Student_mob:
        x=Student_mob.student_id
        getidfromx=db.query(StudentGrade).filter(StudentGrade.student_id==x).first()
        return getidfromx
    return{"message":"no"}

@app.post("/postgrade")
def postgrademob(x:schemas.mobgrade,db: Session = Depends(get_db)):
    student =db.query(s.Student).filter(s.Student.student_mobile_number==x.mob).first()
    s_id= student.student_id
    postgrade=db.query(s.StudentGrade).filter(s.StudentGrade.student_id==s_id).first()
    if postgrade:
        postgrade.student_garde_in_c = x.student_grade_in_c
        postgrade.student_grade_in_python = x.student_grade_in_python
        postgrade.student_grade_in_java = x.student_grade_in_java
        db.commit()
        db.refresh(postgrade)
        return postgrade
    raise HTTPException(status_code=404, detail="Student not found")


# @app.post("/postemailgrade")
# def postgradeemail(x:schemas.emailgrade,db:Session=Depends(get_db)):
#     student=db.query(s.Student).filter(s.Student.student_email_id==x.email).first()
#     if student:
#         student_grade=s.StudentGrade(student_garde_in_c = x.student_grade_in_c,
#                                             student_grade_in_python = x.student_grade_in_python,
#                                             student_grade_in_java = x.student_grade_in_java,
#                                             student_id = student.student_id)
#         db.add(student_grade)
#         db.commit()this code is not updating the grade but creating grade for the studentr̥r̥
#         db.refresh(student_grade)
#         return student_grade
#     raise HTTPException(status_code=404, detail="Student not found")
@app.post("/postemailgrade")
def postgradeemail(x: schemas.emailgrade, db: Session = Depends(get_db)):
    student=db.query(s.Student).filter(s.Student.student_email_id==x.email).first()
    s_id= student.student_id
    postgrade=db.query(s.StudentGrade).filter(s.StudentGrade.student_id==s_id).first()
    if postgrade:
        postgrade.student_garde_in_c = x.student_grade_in_c
        postgrade.student_grade_in_python = x.student_grade_in_python
        postgrade.student_grade_in_java = x.student_grade_in_java
        db.commit()
        db.refresh(postgrade)
        return postgrade
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/parentdetails/")
def create_parent_detail(x:schemas.parentdetails,db:Session=Depends(get_db)):
    student=db.query(s.Student).filter(s.Student.student_id==x.student_id).first()
    if student:
        parent_detail=s.parentdetails(parent_name=x.parent_name,
                                            parent_mobile_number=x.parent_mobile_number,
                                            parent_email_id=x.parent_email_id,
                                            student_id=x.student_id)
        db.add(parent_detail)
        db.commit()
        db.refresh(parent_detail)
        return parent_detail
    raise HTTPException(status_code=404, detail="Student not found")