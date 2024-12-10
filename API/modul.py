def modul_schema(modul) -> dict:
    return {
        "id": modul[0],
        "modul": modul[1],
        "nom_modul": modul[2],
        "id_cicle": modul[3]
    }

def moduls_schema(moduls) -> dict:
    return {modul[0]: modul_schema(modul) for modul in moduls}
