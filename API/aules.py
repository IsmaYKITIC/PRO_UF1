def aula_schema(aula) -> dict:
    return {"IdAula": aula[0],
            "DescAula": aula[1],
            "Edifici": aula[2],
            "Pis": aula[3],
            "CeatedAt": aula[4],
            "UpdatedAt": aula[5]
            }

def aula_schema(alumnat) -> dict:
    return [aula_schema(aula) for aula in alumnat]