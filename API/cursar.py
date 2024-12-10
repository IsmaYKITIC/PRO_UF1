def cursar_schema(cursar) -> dict:
    return {
        "id": cursar[0],
        "id_alumne": cursar[1],
        "id_grup": cursar[2]
    }

def cursars_schema(cursars) -> dict:
    return {cursar[0]: cursar_schema(cursar) for cursar in cursars}
