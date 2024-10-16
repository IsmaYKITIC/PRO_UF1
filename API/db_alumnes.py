from client import db_client
#GET
def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from alumnes")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes
#GET ID
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from aulmes WHERE IdAlumne = %s"
        value = (id,)
        cur.execute(query,value)
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes
#POST
def create(IdAula,NomAlumne,Cicle,Curs,Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumnes (IdAula,NomAlumne,Cicle,Curs,Grup) VALUES (%s,%s,%s,%s,%s);"
        values=(IdAula,NomAlumne,Cicle,Curs,Grup)
        cur.execute(query,values)
    
        conn.commit()
        nouId = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return nouId
#PUT
def update_vots(titol,vots):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update PELICULA SET votos = %s WHERE titulo = %s;"
        values=(vots,titol)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs


#Delete
def delete(IdAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "delete from alumne where IdAlumne = %s;"
        valor = (IdAlumne,)
        cur.execute(query,valor)
        deleted_recs = cur.rowcount
        conn.commit()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return deleted_recs