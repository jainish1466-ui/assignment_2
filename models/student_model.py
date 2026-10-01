from pydantic import BaseModel
from typing import Optional


# Student model
class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    course: str
    semester: int