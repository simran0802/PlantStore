from typing import Optional
from fastapi import FastAPI, datastructures
from pydantic import BaseModel

class plant(BaseModel):
    plantname: str
    type: str
    category: str
    price: int

app = FastAPI()

plantlist = []
selectedplantList = []

@app.get("/index")
def index():
    return {"message" :"Welcome to plant Store!"}

@app.get("/")
def hello():
    return {"message" : "Hello world!"}

@app.get("/plantstore")
def plantstore():
    return plantlist

@app.post("/plantstore")
def insert(plant : plant):
    plantlist.append(plant)
    return plantlist[-1]

@app.get("/billCounter")
def billCounter():
    data = []
    data.append(selectedplantList)
    total = sum(map(lambda b : b.price, selectedplantList)):

    #for plant in selectedplantList:
    #    total += plant['price']

    data.append(dict({"total" : total}))
    return data

@app.post("/billCounter/{id}")
def total(id):
    selectedplantList.append(getplantById(id))
    return selectedplantList[-1]


def getplantById(id):
    return plantlist[int(id) - 1]