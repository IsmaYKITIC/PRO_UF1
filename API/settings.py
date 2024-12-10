#Leer 1
def settings_schema(settings) -> dict:
    return {
        "id": settings[0],
        "id_usuari": settings[1],
        "idioma": settings[2],
        "mode": settings[3]
    }

def settings_schema_multiple(settings_list) -> dict:
    return {settings[0]: settings_schema(settings) for settings in settings_list}