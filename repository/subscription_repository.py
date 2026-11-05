from psycopg import Error
from db import db
from db.db import Database

def get_subscription():
        with Database().connection.cursor() as cursor:
                cursor.execute("SELECT * FROM SUBSCRIPTION")
                users = cursor.fetchall()
                return users    
            
def create_user(email, last_name, role):
    with Database().connection.cursor() as cursor:
        cursor.execute("""
                       INSERT INTO users(email, last_name, role)
                       VALUES (%s,%s,%s)
                       RETURNING id
                       """,
                       (email,last_name,role)
                       )
        user_id = cursor.fetchone()[0]
        return user_id

def delete_user():
    with Database().connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s",(id,))
        rows_count = cursor.rowcount
        return rows_count
    
     
def get_users_manual():
    try:
        conn = None
        conn = Database().connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
                #return users    
        conn.commit()        
    except Error as e:
        
        if conn is not None:
        #SI pas d'erreurs
            conn.rollback()
    else:

        return users
    finally:
        print("finally")
        if cursor is not None:
            conn.close()    
                
