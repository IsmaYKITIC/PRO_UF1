#Leer 1
def aula_schema(aula) -> dict:
    return {"IdAula": aula[0],
            "DescAula": aula[1],
            "Edifici": aula[2],
            "Pis": aula[3],
            "CeatedAt": aula[4],
            "UpdatedAt": aula[5]
            }
#Leer +1
def aules_schema(aules) -> dict:
    return [aula_schema(aula) for aula in aules]