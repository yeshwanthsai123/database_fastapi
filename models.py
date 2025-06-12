from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

 
class Student(Base):
     
    __tablename__="students"
    
    student_id=Column(Integer,primary_key=True,index=True)
    student_name =Column(String)
    student_mobile_number=Column(Integer)
    student_date_of_birth=Column(Integer)
    student_email_id=Column(String)
    student_grade=relationship("StudentGrade",back_populates="student")
    parent_details=relationship("parentdetails", back_populates="student")
    
class StudentGrade(Base):
    
    __tablename__="student_grades"
    
    id = Column(Integer, primary_key=True, index=True)
    student_grade_in_python=Column(Integer)
    student_grade_in_java=Column(Integer)
    student_garde_in_c=Column(Integer)
    student_id=Column(Integer,ForeignKey("students.student_id"))
    student=relationship("Student",back_populates="student_grade")
 
class parentdetails(Base):
    
    __tablename__="parent_details"
    
    parent_id=Column(Integer,primary_key=True,index=True)
    parent_name=Column(String)
    parent_mobile_number=Column(Integer)
    parent_email_id=Column(String)
    student_id=Column(Integer,ForeignKey("students.student_id"))
    student=relationship("Student",back_populates="parent_details")