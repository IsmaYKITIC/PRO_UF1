def grup_schema(grup) -> dict:
    return {
        "id": grup[0],
        "lletra": grup[1],
        "curs": grup[2],
        "id_cicle": grup[3],
        "horari": grup[4]
    }

def grups_schema(grups) -> dict:
    return {grup[0]: grup_schema(grup) for grup in grups}