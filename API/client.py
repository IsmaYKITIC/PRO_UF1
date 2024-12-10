import mysql.connector

def db_client():
    
    try:
        dbname = "alumnat"
        user = "admin"
        password = "admin"
        host = "192.168.35.1"
        port = "5432"
        collation = "utf8mb4_general_ci"
        
        return mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = dbname,
            collation = collation
        ) 
            
    except Exception as e:
            return {"status": -1, "message": f"Error de connexió:{e}" }
