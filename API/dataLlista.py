def data_llista_schema(data_llista) -> dict:
    return {
        "id": data_llista[0],
        "data": data_llista[1],
        "id_llista": data_llista[2]
    }

def data_llistes_schema(data_llistes) -> dict:
    return {data_llista[0]: data_llista_schema(data_llista) for data_llista in data_llistes}
