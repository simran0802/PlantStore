from typing import Optional
from fastapi import FastAPI, datastructures
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    bookname: str
    author: str
    price: int

app = FastAPI()

booklist = []
selectedBookList = []

@app.get("/index")
def index():
    return {"message" :"Welcome to Book Store!"}

@app.get("/")
def hello():
    return {"message" : "Hello world!"}

@app.get("/bookstore")
def bookstore():
    return booklist

@app.post("/bookstore")
def insert(book : Book):
    booklist.append(book)
    return booklist[-1]

@app.get("/billCounter")
def billCounter():
    data = []
    data.append(selectedBookList)
    total = sum(map(lambda b : b.price, selectedBookList))

    #for book in selectedBookList:
    #    total += book['price']

    data.append(dict({"total" : total}))
    return data

@app.post("/billCounter/{id}")
def total(id):
    selectedBookList.append(getBookById(id))
    return selectedBookList[-1]


def getBookById(id):
    return booklist[int(id) - 1]

