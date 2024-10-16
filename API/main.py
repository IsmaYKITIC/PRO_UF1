from fastapi import FastAPI,HTTPException

import db_alumnes 
import alumnes
import aules


from typing import List

from pydantic import BaseModel

app = FastAPI()

class estudiant(BaseModel):
    Idalumne:str
    IdAula: int
    nomAlumne: str
    cicle: str
    curs: int
    grup: str 
#get
@app.get("/")
def read_root():
    return {"API del Alumnat"}

@app.get("/show_alumnes", response_model=List[dict])
def read_pelis():

    pdb = db_alumnes.read()

    alumnes_sch = alumnes.alumne_schema(pdb)

    return alumnes_sch


@app.get("/show_alumnes/{id}", response_model=estudiant)
def read_pelis_id(id:int):
    alumne_data = db_alumnes.read_id(id)
    if db_alumnes.read_id(id) is not None:
        alumne = alumne.alumne_schema(alumne_data)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return alumne

#POST

@app.post("/create_alumne")
async def create_film(data: estudiant):

    IdAula = data.IdAula
    Nom = data.nomAlumne
    Cicle = data.cicle
    Curs = data.curs
    Grup = data.grup
  

    l_alumne_id = db_alumnes.create(IdAula,Nom,Cicle,Curs,Grup)
    return {
        "msg": "alumne creat",
        "id film": l_alumne_id,
        "NomAlumne": Nom
    }

#PUT



