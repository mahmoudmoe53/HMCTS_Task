# HMCTS Task Manager

A simple task management system for caseworkers to create, view, update, and delete tasks. Built with **Python Flask**, **PostgreSQL**, and a vanilla **HTML/JS frontend**.  

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [API Endpoints](#api-endpoints)
7. [Technical Decisions](#technical-decisions)
8. [Future Enhancements](#future-enhancements)

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

While in the parent folder run:
```bash
python -m HMCTS_Task.app
```

**Visit in your browser:**

```cpp
http://127.0.0.1:5000/
```
**You can now**:

Add tasks

View all tasks

Mark tasks as done

Delete tasks

## **Testing**

**Run tests using pytest:**
```bash
pytest
```

tests/test_taskdb.py → tests database CRUD operations

tests/test_app.py → tests API routes

## **API Endpoints**
**Method**	**Route**	**Description**
POST	/api/tasks	Create a new task
GET	/api/tasks	Retrieve all tasks
GET	/api/tasks/<id>	Retrieve a single task
PATCH	/api/tasks/<id>	Update task status
DELETE	/api/tasks/<id>	Delete a task

## **Technical Decisions**

**Flask:** Lightweight and easy to set up for APIs and serving frontend. Good for a small proof-of-concept system.

**OOP Design:** TaskDB class encapsulates all database interactions, making code modular, testable, and easy to extend.

**psycopg2:** Direct PostgreSQL interaction without heavy ORM. Keeps the system simple and explicit for a small challenge.

**Frontend:** Vanilla JS + HTML to keep the UI simple while still functional, allows users to interact with tasks in the browser.

**Testing:** Pytest for both database and API ensures reliable functionality before deployment.

**Trade-offs:**

No ORM like SQLAlchemy → less abstraction but simpler for a small project.

Vanilla JS frontend → minimal, but enough to meet requirements without introducing complexity.

No authentication → out of scope for challenge, but can be added later for real-world deployment.

## **Future Enhancements**

Edit task title and description via frontend.

Sort and filter tasks by status or due date.

Integrate GOV.UK Design System for consistent UI.

Add authentication for caseworkers.

Deploy to Azure or containerize with Docker for production.

Author: Mahmoud
Submission for HMCTS Technical Test
