from psycopg import Error
from db import db
from db.db import Database

def get_followcourse():
        with Database().connection.cursor() as cursor:
                cursor.execute("""
                                SELECT u.last_name as "Nom",
                                       t.description as "Cours suivi",
                                       t.hour_start As "Début",
                                       t.hour_end As "Fin",
                                       case t.day 
                                          WHEN 1 THEN 'Monday'
                                          WHEN 2 THEN 'Tuesday'
                                          WHEN 3 THEN 'Wednesday'
                                          WHEN 4 THEN 'Thursday'
                                          WHEN 5 THEN 'Friday'
                                          WHEN 6 THEN 'Saturday'
                                          WHEN 7 THEN 'Sunday'
                                          ELSE 'Inconnu'
                                       END AS "day"
                                       FROM followcourse fc
                                       INNER JOIN users u ON fc.user_id = u.id
                                       INNER JOIN training t ON fc.training_id = t.id                               
                               """)
                users = cursor.fetchall()
                return users    
            
def create_followcourse(user_id, training_id):
    with Database().connection.cursor() as cursor:
        cursor.execute("""
                       INSERT INTO followcourse(user_id, training_id)
                       VALUES (%s,%s)         
                       """,
                       (user_id, training_id)
                       )
        #followcourse_id = cursor.fetchone()[0]
        rows_count = cursor.rowcount
        return rows_count

def delete_followcourse(id):
    with Database().connection.cursor() as cursor:
        cursor.execute("DELETE FROM subscription WHERE id = %s",(id,))
        rows_count = cursor.rowcount
        return rows_count
    
