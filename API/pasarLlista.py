def pasar_llista_schema(pasar_llista) -> dict:
    return {
        "id": pasar_llista[0],
        "id_professor": pasar_llista[1],
        "id_alumne": pasar_llista[2]
    }

def pasar_llistes_schema(pasar_llistes) -> dict:
    return {pasar_llista[0]: pasar_llista_schema(pasar_llista) for pasar_llista in pasar_llistes}
