import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def get_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s;"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            if user:
                print(f"User found: {user}")
            else:
                print("No user found.")
            cursor.close()
        except Exception as e:
            print(f"Error retrieving user: {e}")
        finally:
            conn.close()

#get_user(1)
