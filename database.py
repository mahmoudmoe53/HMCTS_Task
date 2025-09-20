import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

class TaskDB:
    def __init__(self):
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL is not set in your environment.")

    def get_connection(self):
        """Return a new psycopg2 database connection."""
        return psycopg2.connect(DATABASE_URL)

    def initialise_db(self):
        """Reset the tasks table (drop and recreate)."""
        conn = self.get_connection()
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
        cur.close()
        conn.close()

    def create_task(self, title, description=None, status="todo", due_date=None):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, description, status, due_date) VALUES (%s, %s, %s, %s) RETURNING id;",
            (title, description, status, due_date)
        )
        task_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return task_id

    def get_task(self, task_id):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, description, status, due_date FROM tasks WHERE id=%s;",
            (task_id,)
        )
        task = cur.fetchone()
        cur.close()
        conn.close()
        return task


    def get_all_tasks(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, description, status, due_date FROM tasks ORDER BY due_date NULLS FIRST;"
        )
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return tasks


    def update_task_status(self, task_id, new_status):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE tasks SET status=%s WHERE id=%s RETURNING id;",
            (new_status, task_id)
        )
        updated = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return updated

    def delete_task(self, task_id):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM tasks WHERE id=%s RETURNING id;",
            (task_id,)
        )
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return deleted
