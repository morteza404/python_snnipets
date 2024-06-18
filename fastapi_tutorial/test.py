from pydantic import BaseModel, Field
from typing import List


class Student(BaseModel):
    id: int
    name: str = Field(..., title="Name", min_length=3, max_length=10)
    subjects: List[str] = []


data = {
    "id": 1,
    "name": "Morteza",
    "subjects": ["Eng", "Maths", "Sci"],
}

student = Student(**data)
print(student)
