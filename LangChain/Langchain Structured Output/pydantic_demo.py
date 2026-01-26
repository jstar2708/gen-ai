from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {"name": "Jaideep", "email": "123@gmail.com", "cgpa": 5}

student = Student(**new_student)
print(student)

# Data is validated and if you try to pass int instead of string then it will
# raise an error.



