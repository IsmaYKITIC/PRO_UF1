#Leer uno
def cicle_schema(cicle) -> dict:
    return {
        "id": cicle[0],
        "nom": cicle[1]
    }

def cicles_schema(cicles) -> dict:
    return {cicle[0]: cicle_schema(cicle) for cicle in cicles}
