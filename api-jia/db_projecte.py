from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from usuaris")
    
        films = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return films

def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from usuaris WHERE id = %s"
        value = (id,)
        cur.execute(query,value)
    
        film = cur.fetchone()

    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return film