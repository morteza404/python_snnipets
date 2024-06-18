import uvicorn
from fastapi import FastAPI, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    publisher = Column(String(50))


Base.metadata.create_all(bind=engine)


class Book(BaseModel):
    title: str
    author: str
    publisher: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/add_new", response_model=Book)
def add_book(b1: Book, db: Session = Depends(get_db)):
    bk = Books(title=b1.title, author=b1.author, publisher=b1.publisher)
    db.add(bk)
    db.commit()
    db.refresh(bk)
    return b1


@app.get("/list", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Books).all()
    return books


@app.get("/book/{id}", response_model=Book)
def get_book(id: int, db: Session = Depends(get_db)):
    return db.query(Books).filter(Books.id == id).first()


@app.put("/update/{id}", response_model=Book)
def update_book(id: int, book: Book, db: Session = Depends(get_db)):
    b1 = db.query(Books).filter(Books.id == id).first()
    b1.title = book.title
    b1.author = book.author
    b1.publisher = book.publisher
    db.commit()
    return db.query(Books).filter(Books.id == id).first()


@app.delete("/delete/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    try:
        db.query(Books).filter(Books.id == id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"delete status": "success"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8040)
