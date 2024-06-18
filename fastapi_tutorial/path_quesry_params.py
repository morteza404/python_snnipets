import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int


@app.get("/items/{item}")
async def read_items(item:str):
    return {"message": f"Hello, {item}!"}       
    

@app.get("/")
async def root(param:str):
    return {"message": f"Hello, {param}!"}

@app.post("/")
async def create(body:Person=Body()):
    return body

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8010)