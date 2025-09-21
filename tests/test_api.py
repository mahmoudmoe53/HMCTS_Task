import pytest
from HMCTS_Task.app import app
from HMCTS_Task.database import TaskDB

@pytest.fixture
def client():
    """Creates a test client and resets the database before each test."""
    task_db = TaskDB()
    task_db.initialise_db()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "Testing Flask route",
        "status": "todo"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data


def test_get_all_tasks(client):
    client.post("/api/tasks", json={"title": "Task 1", "status": "todo"})
    client.post("/api/tasks", json={"title": "Task 2", "status": "todo"})
    response = client.get("/api/tasks")
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["title"] == "Task 2"


def test_get_task(client):
    res = client.post("/api/tasks", json={"title": "Single Task", "status": "todo"})
    task_id = res.get_json()["id"]
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    task = response.get_json()
    assert task["id"] == task_id
    assert task["title"] == "Single Task"


def test_update_task_status(client):
    res = client.post("/api/tasks", json={"title": "Update Task", "status": "todo"})
    task_id = res.get_json()["id"]
    response = client.patch(f"/api/tasks/{task_id}", json={"status": "done"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "done"


def test_delete_task(client):
    res = client.post("/api/tasks", json={"title": "Delete Task", "status": "todo"})
    task_id = res.get_json()["id"]
    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 404

