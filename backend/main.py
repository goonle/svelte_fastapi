from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
    name : str
    price: float
    is_offer : Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) :
    return {"item_id" : item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item):
    return { "item_name": item.name, "item_id": item_id}

@app.get("/hello")
def hello():
    return { "message" : "안녕하세요 파이보"}