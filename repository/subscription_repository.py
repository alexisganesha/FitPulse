from psycopg import Error
from db import db
from db.db import Database

def get_subscription():
        with Database().connection.cursor() as cursor:
                cursor.execute("SELECT * FROM SUBSCRIPTION")
                users = cursor.fetchall()
                return users    
            
def create_subscription(type, prix, duree):
    with Database().connection.cursor() as cursor:
        cursor.execute("""
                       INSERT INTO subscription(type, prix, duree)
                       VALUES (%s,%s,%s)
                       RETURNING id
                       """,
                       (type, prix, duree)
                       )
        subscription_id = cursor.fetchone()[0]
        return subscription_id

def delete_subscription(id):
    with Database().connection.cursor() as cursor:
        cursor.execute("DELETE FROM subscription WHERE id = %s",(id,))
        rows_count = cursor.rowcount
        return rows_count
    
                
