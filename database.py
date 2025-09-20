import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in your environment.")
    return psycopg2.connect(DATABASE_URL)

def initialise_db():
    conn = get_db_connection()
    cur = None
    try:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS tasks;')
        cur.execute('''
            CREATE TABLE tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                status VARCHAR(50) NOT NULL,
                due_date TIMESTAMP
            );
        ''')
        conn.commit()
    finally:
        if cur:
            cur.close()
        conn.close()

