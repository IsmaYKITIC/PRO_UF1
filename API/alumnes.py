def alumne_schema(alumne) -> dict:
    return {
        "Idalumne": alumne[0],
        "Descalumne": alumne[1],
        "Edifici": alumne[2],
        "Pis": alumne[3],
        "CeatedAt": alumne[4],
        "UpdatedAt": alumne[5]
    }

def alumnat_schema(alumnat) -> dict:
    return [alumne_schema(alumne) for alumne in alumnat]