import psycopg2
from psycopg2 import sql,OperationalError
import psycopg2.extras

import os
from dotenv import load_dotenv
load_dotenv()
conn=None
#function to connect to the database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            database=os.getenv('DATABASE'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
        )
        print("Connection to PostgreSQl DB successful")
        return conn
    
    except OperationalError as e:
        print(f"the error '{e}'occured")
        return None
    # finally:
    #     if conne
conn=get_db_connection()