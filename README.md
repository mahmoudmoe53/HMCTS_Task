# HMCTS Task Manager

A simple task management system for caseworkers to create, view, update, and delete tasks. Built with **Python Flask**, **PostgreSQL**, and a vanilla **HTML/JS frontend**.  

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Running with Docker](#running-with-docker)
6. [Testing](#testing)
7. [API Endpoints](#api-endpoints)
8. [Technical Decisions](#technical-decisions)
9. [Future Enhancements](#future-enhancements)

---

## **Project Overview**
This project implements a lightweight task tracking system for HMCTS caseworkers:

- Create tasks with a title, optional description, status, and due date/time.
- View all tasks or a single task.
- Update task status.
- Delete tasks.
- Frontend UI allows interaction without Postman or curl.

---

## **Technologies Used**
- **Backend:** Python, Flask
- **Database:** PostgreSQL with `psycopg2`
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Testing:** Pytest
- **Environment Variables:** `python-dotenv` to manage database credentials

---

## **Setup Instructions**

1. **Clone the repository**
```bash
git clone https://github.com/mahmoudmoe53/HMCTS_Task.git
cd HMCTS_Task
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```


3. **Set up the database**

Create a PostgreSQL database for the app.

Create a .env file in the project root:
```dotenv
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

4. **Initialize the database**
```python
from initialise_db import initialise_db
initialise_db()
```


## **Running the Application**

**Start the Flask app:**

While in the root directory:
```bash
python app.py
```

**Visit in your browser:**

```cpp
http://127.0.0.1:5001/
```
**You can now**:

Add tasks

View all tasks

Mark tasks as done

Delete tasks

## **Running with Docker**

**Build the Docker image:**
```bash
docker build -t hmcts-task-app .
```

**Run the container:**
```bash
docker run -p 5001:5001 --env-file .env hmcts-task-app
```



Note: Make sure the .env file is correctly set up so the Flask app can connect to PostgreSQL.

**Visit in your browser:**

http://localhost:5001/


Optional: Connect to a separate PostgreSQL container by updating DATABASE_URL in .env to point to the container host.



## **Testing**

**Run tests using pytest:**
```bash
pytest
```

tests/test_database.py → tests database CRUD operations

tests/test_api.py → tests API routes

## **API Endpoints**
| Method | Route           | Description           |
|--------|-----------------|---------------------|
| POST   | /api/tasks      | Create a new task   |
| GET    | /api/tasks      | Retrieve all tasks  |
| GET    | /api/tasks/<id> | Retrieve a single task |
| PATCH  | /api/tasks/<id> | Update task status  |
| DELETE | /api/tasks/<id> | Delete a task       |


## **Technical Decisions**

**Flask:** Lightweight and easy to set up for APIs and serving frontend. Good for a small proof-of-concept system.

**OOP Design:** TaskDB class encapsulates all database interactions, making code modular, testable, and easy to extend.

**psycopg2:** Direct PostgreSQL interaction without heavy ORM. Keeps the system simple and explicit for a small challenge.

**Frontend:** Vanilla JS + HTML to keep the UI simple while still functional, allows users to interact with tasks in the browser.

**Testing:** Pytest for both database and API ensures reliable functionality before deployment.


## **Future Enhancements**

- Edit task title and description via the frontend for better task management.
- Sort and filter tasks by status or due date for easier task tracking.
- Integrate the **GOV.UK Design System** for a consistent, professional UI.
- Add authentication and role-based access control for caseworkers.
- **Containerized PostgreSQL:** Run PostgreSQL inside a Docker container alongside the Flask app for easier development and deployment.
- **Kubernetes deployment:** Use Kubernetes to orchestrate containers, manage scaling, and ensure high availability.
- **CI/CD Pipelines:** Implement automated testing, building, and deployment using GitHub Actions or Jenkins.
- **Cloud Deployment:** Deploy the application to cloud platforms like AWS, Azure, or GCP for production, taking advantage of managed databases, container services, and load balancers.
- Implement **automated backups and monitoring** for production databases and containers to ensure reliability.
- Extend testing coverage with integration tests to ensure the frontend and backend work seamlessly together.


Author: Mahmoud
Submission for HMCTS Technical Test
