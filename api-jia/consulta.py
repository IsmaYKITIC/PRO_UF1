def consulta_schema(consulta) -> dict:
    return {
        "id": consulta[0],
        "id_usuari": consulta[1],
        "id_modul": consulta[2]
    }

def consultes_schema(consultes) -> dict:
    return {consulta[0]: consulta_schema(consulta) for consulta in consultes}
