import uvicorn
from fastapi import FastAPI, Path, Form
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(..., title="Name", min_length=3, max_length=10)
    subjects: List[str] = []

class User(BaseModel):
   username:str
   password:str


@app.get("/")
async def index():
    return {"message": "Hello World"}


# Path Parameters
# http://0.0.0.0:8010/hello/morteza/33
@app.get("/hello/{name}/{age}")
async def hello(name: str, age: int):
    return {"name": name, "age": age}


# Query Parameters
# http://0.0.0.0:8010/bye?name=morteza&age=33
@app.get("/bye")
async def bye(name: str, age: int):
    return {"name": name, "age": age}


# Parameter Validation (by using Path)
@app.get("/goodbye/{name}")
async def goodbye(
    name: str = Path(
        ..., min_length=3, max_length=10, description="The name of the user to greet"
    )
):
    return {"name": name}


@app.post("/students/")
async def student_data(student: Student):
    return student


@app.post("/submit/", response_model=User)
async def submit(username: str = Form(...), password: str = Form(...)):
   return User(username=username, password=password)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
