from psycopg import Error
from db import db
from db.db import Database

def get_followcourse():
        with Database().connection.cursor() as cursor:
                cursor.execute("""
                                SELECT u.last_name as "Nom",
                                       t.description as "Cours suivi",
                                       t.hour_start As "Début"
                                       FROM followcourse fc
                                       INNER JOIN users u ON fc.user_id = u.id
                                       INNER JOIN training t ON fc.training_id = t.id                               
                               """)
                users = cursor.fetchall()
                return users    
            
def create_followcourse(type, prix, duree):
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

def delete_followcourse(id):
    with Database().connection.cursor() as cursor:
        cursor.execute("DELETE FROM subscription WHERE id = %s",(id,))
        rows_count = cursor.rowcount
        return rows_count
    
                
