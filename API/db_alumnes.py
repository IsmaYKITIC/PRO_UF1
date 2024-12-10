from client import db_client
#GET
def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from usuaris")
    
        usuaris = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return usuaris
#GET ID
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select IdAlumne,IdAula, NomAlumne, Cicle, Curs, Grup from alumne WHERE IdAlumne = %s"
        value = (id,)
        cur.execute(query,value)
    
        alumne = cur.fetchone()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumne
#POST
def create(IdAula,NomAlumne,Cicle,Curs,Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumne (IdAula,NomAlumne,Cicle,Curs,Grup) VALUES (%s,%s,%s,%s,%s);"
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
def update_alumne(IdAlumne,IdAulaN,NomAlumneN,CicleN,CursN,GrupN):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update alumne SET IdAula = %s, NomAlumne =%s , Cicle = %s, Curs = %s, Grup = %s WHERE IdAlumne = %s;"
        values=(IdAulaN,NomAlumneN,CicleN,CursN,GrupN,IdAlumne)
        cur.execute(query,values)
        updated_recs = cur.rowcount()
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs


#Delete
def delete_alumnes(IdAlumne):
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