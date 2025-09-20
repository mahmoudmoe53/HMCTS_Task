import pytest
from psycopg2 import OperationalError
from database import get_db_connection

def test_db_connection():
    try:
        conn = get_db_connection()
        assert conn.status == 1
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
