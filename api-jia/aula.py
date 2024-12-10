#Leer uno
def aula_schema(aula) -> dict:
    return {
        "id": aula[0],
        "nom": aula[1]
    }

#Leer mas de uno
def aules_schema(aules) -> dict:
    return {aula[0]: aula_schema(aula) for aula in aules}
