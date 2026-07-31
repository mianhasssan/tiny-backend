# 🚀 Tiny Backend API with SQLite

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-Educational-green)

A lightweight RESTful API built with **Python**, **Flask**, and **SQLite** that demonstrates complete CRUD (Create, Read, Update, Delete) operations. This project was developed as part of the **FlyRank Backend Internship** to learn backend development, database integration, REST APIs, SQL, and GitHub workflow.

---

# 📖 Project Overview

This project demonstrates how a backend application communicates with a SQLite database to store and manage persistent data.

Unlike Assignment 1, where tasks were stored in memory and disappeared after restarting the server, this version stores all tasks inside a SQLite database (`tasks.db`), allowing data to persist across application restarts.

---

# ✨ Features

- ✅ Flask REST API
- ✅ SQLite Database Integration
- ✅ Complete CRUD Operations
- ✅ Persistent Data Storage
- ✅ Automatic Database Creation
- ✅ Automatic Table Creation
- ✅ Automatic Sample Data Seeding
- ✅ JSON Responses
- ✅ Input Validation
- ✅ Proper HTTP Status Codes
- ✅ Parameterized SQL Queries
- ✅ Browser & cURL Testing
- ✅ SQL Practice with DB Browser for SQLite

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Flask | Backend Framework |
| SQLite3 | Local Database |
| DB Browser for SQLite | Database Viewer |
| Git | Version Control |
| GitHub | Source Code Hosting |
| cURL | API Testing |

---

# 📂 Project Structure

```text
tiny-backend/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── images/
│   └── database.png
└── tasks.db (created automatically)
```

---

# 💡 Why SQLite?

SQLite was chosen because it is:

- Lightweight
- Serverless
- Zero configuration
- Fast for small projects
- Stores everything inside one database file
- Perfect for learning backend development

Unlike storing data in Python lists, SQLite keeps data even after restarting the application.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/tiny-backend.git
```

```bash
cd tiny-backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Start the Flask server:

```bash
python app.py
```

Server URL

```
http://127.0.0.1:5000
```

The application automatically:

- Creates `tasks.db`
- Creates the `tasks` table
- Inserts three sample tasks (only if the table is empty)

No manual database setup is required.

---

# 🗄 Database

Database File

```
tasks.db
```

The database file is automatically generated the first time the application runs.

Table Structure

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
);
```

---

# 🌐 API Endpoints

## Get All Tasks

```http
GET /tasks
```

Response

```json
[
    {
        "id":1,
        "title":"Learn SQLite",
        "done":0
    }
]
```

---

## Get Single Task

```http
GET /tasks/1
```

---

## Create Task

```http
POST /tasks
```

Request

```json
{
    "title":"Learn Flask"
}
```

Response

```json
{
    "id":4,
    "title":"Learn Flask",
    "done":0
}
```

Status Code

```
201 Created
```

---

## Update Task

```http
PUT /tasks/4
```

Request

```json
{
    "title":"Learn Flask Updated",
    "done":true
}
```

Response

```json
{
    "id":4,
    "title":"Learn Flask Updated",
    "done":1
}
```

Status Code

```
200 OK
```

---

## Delete Task

```http
DELETE /tasks/4
```

Response

```
204 No Content
```

---

# ❌ Error Handling

## Task Not Found

```json
{
    "error":"Task not found"
}
```

Status

```
404 Not Found
```

---

## Missing Title

```json
{
    "error":"Title is required"
}
```

Status

```
400 Bad Request
```

---

# 🧪 Testing

## Browser

```
http://127.0.0.1:5000/tasks
```

```
http://127.0.0.1:5000/tasks/1
```

---

## cURL

### Get Tasks

```bash
curl http://127.0.0.1:5000/tasks
```

### Create Task

```bash
curl -X POST http://127.0.0.1:5000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Learn Flask\"}"
```

### Update Task

```bash
curl -X PUT http://127.0.0.1:5000/tasks/4 ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Updated Task\",\"done\":true}"
```

### Delete Task

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/4
```

---

# 💻 SQL Practice

During this assignment, SQL queries were executed directly using **DB Browser for SQLite**.

### View All Tasks

```sql
SELECT * FROM tasks;
```

Displays every task stored in the database.

---

### View Completed Tasks

```sql
SELECT * FROM tasks
WHERE done = 1;
```

Returns only completed tasks.

---

### Count Tasks

```sql
SELECT COUNT(*) FROM tasks;
```

Returns the total number of tasks stored in the database.

---

### Mark All Tasks as Completed

```sql
UPDATE tasks
SET done = 1;
```

Updates every task in the database.

---

### Delete Completed Tasks

```sql
DELETE FROM tasks
WHERE done = 1;
```

Deletes all completed tasks.

---

# 📷 Database Screenshot

Open **DB Browser for SQLite** and include a screenshot of your database here.

Example:

```
images/database.png
```

```markdown
![Database Screenshot](images/database.png)
```

---

## PostgreSQL with Docker

This project now uses PostgreSQL running inside a Docker container instead of SQLite.

### Start PostgreSQL

```bash
docker run --name taskdb -e POSTGRES_PASSWORD=dev -e POSTGRES_DB=tasks -p 5432:5432 -v taskdata:/var/lib/postgresql/data -d postgres:17

# 📚 What I Learned

Through this project, I learned how to:

- Build REST APIs using Flask
- Perform CRUD operations
- Connect Flask with SQLite
- Create databases automatically
- Seed initial data
- Execute SQL queries
- Use parameterized SQL statements
- Return JSON responses
- Handle HTTP status codes correctly
- Test APIs using Browser and cURL
- Manage backend projects with Git and GitHub

---

# 🎯 Learning Outcomes

This project strengthened my understanding of:

- Backend Development Fundamentals
- RESTful API Design
- Database Integration
- Persistent Data Storage
- SQL Query Execution
- Flask Routing
- Input Validation
- CRUD Operations
- API Testing
- Version Control

---

# 🚀 Future Improvements

- User Authentication
- JWT Authorization
- Task Categories
- Search & Filtering
- Pagination
- API Documentation (Swagger/OpenAPI)
- Unit Testing with Pytest
- Docker Support
- Cloud Deployment (Render/Railway)

---

# 👨‍💻 Author

**Mian Muhammad Hassan**

Backend Developer | Python Developer

🔗 **GitHub**

```
https://github.com/mianhasssan
```

🔗 **LinkedIn**

```
https://linkedin.com/in/mianhasssan
```

---

# 📜 License

This project was created for educational purposes as part of the **FlyRank Backend Internship Program**.