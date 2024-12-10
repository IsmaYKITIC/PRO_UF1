def usuaris_schema(user) -> dict:
    return {"Id": user[0],
            "titol": user[1],
            "any": user[2],
            "puntuacio": user[3],
            "vots": user[4] 
            }

def usuaris_schema(usuaris) -> dict:
    return [usuaris_schema(usuari) for usuari in usuaris]
def usuaris_schema(user) -> dict:
    return {"Id": user[0],
            "titol": user[1],
            "any": user[2],
            "puntuacio": user[3],
            "vots": user[4] 
            }

def usuaris_schema(usuaris) -> dict:
    return [usuaris_schema(usuari) for usuari in usuaris]