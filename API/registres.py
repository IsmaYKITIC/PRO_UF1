def registre_schema(registre) -> dict:
    return {
        "id": registre[0],
        "id_targeta": registre[1],
        "hora_acces": registre[2],
        "id_alumne": registre[3]
    }

def registres_schema(registres) -> dict:
    return {registre[0]: registre_schema(registre) for registre in registres}
