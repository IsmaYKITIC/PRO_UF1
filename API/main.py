from fastapi import FastAPI,HTTPException

import db_alumnes 
import usuaris
import settings


from typing import List

from pydantic import BaseModel

app = FastAPI()

class estudiant(BaseModel):
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: int
    Grup: str 
#GET
@app.get("/")
def read_root():
    return {"API del Alumnat"}

@app.get("/show_alumnes", response_model=List[dict])
def read_alumnes():

    pdb = db_alumnes.read()

    alumnes_sch = usuaris.alumnes_schema(pdb)

    return alumnes_sch


@app.get("/show_alumnes/{id}", response_model=estudiant)
def read_alumnes_id(id:int):
    alumne_data = db_alumnes.read_id(id)
    if alumne_data is not None:
        alumne = usuaris.alumne_schema(alumne_data)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return alumne

#POST

@app.post("/create_alumne")
async def create_alumne(data: estudiant):

    IdAula = data.IdAula
    Nom = data.NomAlumne
    Cicle = data.Cicle
    Curs = data.Curs
    Grup = data.Grup
  

    l_alumne_id = db_alumnes.create(IdAula,Nom,Cicle,Curs,Grup)
    return {
        "msg": "S’ha afegit correctement",
        "id film": l_alumne_id,
        "NomAlumne": Nom
    }

#PUT
@app.put("/update_alumne/{id}")
def update_alumnes(IdAlumne,IdAula,NomAlumne,Cicle,Curs,Grup):
    updated_records = db_alumnes.update_alumne(IdAlumne,IdAula,NomAlumne,Cicle,Curs,Grup)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="Items to update not found")
    
#DELETE

@app.delete("/delete_alumne/{id}")
def delete_alumne(IdAlumne: int):
    deleted_records = db_alumnes.delete_alumnes(IdAlumne)
    if deleted_records == 0:
        raise HTTPException(status_code=404, detail="Item to delete not found")
    return {"msg": "S’ha eliminat correctament"}

