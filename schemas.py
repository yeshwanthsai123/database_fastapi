from pydantic import BaseModel, Field
from typing import Optional 
 
class StudentGradeBase(BaseModel):
    student_grade_in_python: int
    student_grade_in_java: int
    student_grade_in_c: int
 
class StudentGradeCreate(StudentGradeBase):
    student_id: int
 
class StudentGradeResponse(StudentGradeBase):
    id: int
 
    class Config:
        orm_mode = True
 
 
class StudentBase(BaseModel):
    student_name: str
    student_mobile_number: int
    student_date_of_birth: int
    student_email_id: str
 
class StudentCreate(StudentBase):
    pass   
 
class mobgrade(BaseModel):
    mob:int
    student_grade_in_python: int = None
    student_grade_in_java: int =None
    student_grade_in_c: int =None

class emailgrade(BaseModel):
    email:str
    student_grade_in_python: int = None
    student_grade_in_java: int =None
    student_grade_in_c: int =None

class parentdetails(BaseModel):
    parent_name: str
    parent_mobile_number: int
    parent_email_id: str
    student_id: int