#Leer uno
def usuari_schema(usuari) -> dict:
    return {
        "id": usuari[0],
        "nom": usuari[1],
        "mail": usuari[2],
        "password": usuari[3],
        "direccio": usuari[4],
        "data_naixement": usuari[5],
        "ultim_acces": usuari[6],
        "rol": usuari[7],
        "data_matriculacio": usuari[8]
    }

#Leer mas de uno
def usuaris_schema(usuaris) -> dict:
    return {usuari[0]: usuari_schema(usuari) for usuari in usuaris}