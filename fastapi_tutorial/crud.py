import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data = []


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

@app.post("/book")
def add_book(book: Book):
   data.append(book.model_dump())
   return data

@app.get("/list")
def get_books():
   return data

@app.get("/book/{id}")
def get_book(id: int):
   id = id - 1
   return data[id]

@app.put("/book/{id}")
def update_book(id: int, book: Book):
   data[id-1] = book
   return data

@app.delete("/book/{id}")
def delete_book(id: int):
   data.pop(id-1)
   return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8030)
