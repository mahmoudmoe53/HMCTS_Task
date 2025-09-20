import pytest
from psycopg2 import OperationalError
from HMCTS_Task.database import TaskDB

@pytest.fixture
def db():
    """Create a TaskDB instance and initialise the test database."""
    task_db = TaskDB()
    task_db.initialise_db()
    return task_db

def test_db_connection(db):
    """Test that a connection can be established."""
    try:
        conn = db.get_connection()
        assert conn.status == 1  # psycopg2 status 1 = connection OK
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def test_create_task(db):
    """Test creating a task."""
    task_id = db.create_task(title="Test Task", description="Test description")
    assert task_id is not None

def test_get_task(db):
    """Test retrieving a task by ID."""
    task_id = db.create_task(title="Get Task")
    task = db.get_task(task_id)
    assert task[0] == task_id
    assert task[1] == "Get Task"

def test_get_all_tasks(db):
    """Test retrieving all tasks."""
    db.create_task(title="Task 1")
    db.create_task(title="Task 2")
    tasks = db.get_all_tasks()
    assert len(tasks) == 2

def test_update_task_status(db):
    """Test updating a task's status."""
    task_id = db.create_task(title="Update Task", status="todo")
    updated = db.update_task_status(task_id, "done")
    assert updated[0] == task_id
    task = db.get_task(task_id)
    assert task[3] == "done"

def test_delete_task(db):
    """Test deleting a task."""
    task_id = db.create_task(title="Delete Task")
    deleted = db.delete_task(task_id)
    assert deleted[0] == task_id
    task = db.get_task(task_id)
    assert task is None
