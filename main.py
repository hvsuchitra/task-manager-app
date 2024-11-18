from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello World"}

@app.get("/items/{item_id}")
def getItem(item_id : int, q: Optional[str] = None):
    return{"item_id":item_id, "q":q}

