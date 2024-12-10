import mysql.connector

def db_client():
    
    try:
        dbname = "projecte"
        user = "admin"
        password = "admin"
        host = "localhost"
        port = "5432"
        
        return mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = dbname 
        ) 
            
    except Exception as e:
            return {"status": -1, "message": f"Error de connexió:{e}" }