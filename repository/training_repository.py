from psycopg import Error
from db import db
from db.db import Database

def get_training():
        with Database().connection.cursor() as cursor:
                cursor.execute("SELECT * FROM training")
                users = cursor.fetchall()
                return users    
            
def create_training(description, hour_start, hour_end, day, user_id):
    with Database().connection.cursor() as cursor:
        cursor.execute("""
                       INSERT INTO training (description, hour_start, hour_end, day, user_id)
                       VALUES (%s,%s,%s,%s,%s)
                       RETURNING id
                       """,
                       (description, hour_start, hour_end, day, user_id)
                       )
        training_id = cursor.fetchone()[0]
        return training_id

def delete_training(id):
    with Database().connection.cursor() as cursor:
        cursor.execute("DELETE FROM training WHERE id = %s",(id,))
        rows_count = cursor.rowcount
        return rows_count
    
                
