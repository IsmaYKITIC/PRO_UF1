from fastapi import FastAPI,HTTPException

import db_projecte
import usuaris

from typing import List

from pydantic import BaseModel

app = FastAPI()

class film(BaseModel):
    titol:str
    any: int
    puntuacio: float
    vots: int 

@app.get("/")
def read_root():
    return {"Films API"}

@app.get("/usuaris", response_model=List[dict])
def read_usuaris():
    return usuaris.usuaris_schema(db_projecte.read())

@app.get("/usuaris/{id}", response_model=film)
def read_usuaris_id(id:int):
    if db_projecte.read_id(id) is not None:
        film = usuaris.usuaris_schema(db_projecte.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return film