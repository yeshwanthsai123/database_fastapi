from sqlalchemy.orm import Session
import models, schemas
import models as s
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = s.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
 
def get_student(db: Session, student_id: int):
    return db.query(s.Student).filter(s.Student.student_id == student_id).first()
 
def create_student_grade(db: Session, grade: schemas.StudentGradeCreate):
    db_grade = s.StudentGrade(**grade.dict())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade
 
def get_all_students(db: Session):
    return db.query(s.Student).all()
 