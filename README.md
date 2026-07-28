# 🚀 Tiny Backend API with SQLite

A lightweight **Flask REST API** that demonstrates the fundamentals of backend development using **Python**, **Flask**, and **SQLite**. This project implements a complete **CRUD (Create, Read, Update, Delete)** API with persistent data storage and serves as a practical introduction to RESTful API development.

---

## 📖 Project Overview

This project was developed as part of the **FlyRank Backend Internship** to understand:

- Building REST APIs with Flask
- Working with SQLite databases
- Implementing CRUD operations
- Executing SQL queries
- Testing APIs using Browser and cURL
- Managing projects with Git & GitHub

Unlike the first assignment, where data existed only in memory, this project stores data permanently in a SQLite database (`tasks.db`).

---

# ✨ Features

- ✅ RESTful API
- ✅ SQLite database integration
- ✅ Persistent data storage
- ✅ Complete CRUD operations
- ✅ JSON responses
- ✅ Input validation
- ✅ Proper HTTP status codes
- ✅ Parameterized SQL queries
- ✅ Tested with Browser, cURL & DB Browser for SQLite

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Flask | Backend Framework |
| SQLite3 | Database |
| DB Browser for SQLite | Database Viewer |
| Git | Version Control |
| GitHub | Project Hosting |
| cURL | API Testing |

---

# 📂 Project Structure

```text
tiny-backend/
│
├── app.py
├── database.py
├── tasks.db
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/tiny-backend.git
```

```bash
cd tiny-backend
```

---

## 2️⃣ Create Virtual Environment

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
```

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Server

```bash
python app.py
```

Server runs on

```
http://127.0.0.1:5000
```

---

# 🗄 Database

Database File

```
tasks.db
```

Table

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
);
```

---

# 🌐 API Endpoints

## 📌 Get All Tasks

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

## 📌 Get Single Task

```http
GET /tasks/1
```

---

## 📌 Create Task

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

## 📌 Update Task

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

## 📌 Delete Task

```http
DELETE /tasks/4
```

Response

```
204 No Content
```

---

# ❌ Error Responses

### Task Not Found

```json
{
    "error":"Task not found"
}
```

Status Code

```
404 Not Found
```

---

### Missing Title

```json
{
    "error":"Title is required"
}
```

Status Code

```
400 Bad Request
```

---

# 🧪 Testing the API

## Browser

```
http://127.0.0.1:5000/tasks
```

```
http://127.0.0.1:5000/tasks/1
```

---

## cURL

### Get All Tasks

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

During this assignment SQL queries were executed directly using **DB Browser for SQLite**.

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

Returns the total number of tasks.

---

### Mark All Tasks Completed

```sql
UPDATE tasks
SET done = 1;
```

Updates every task as completed.

---

### Delete Completed Tasks

```sql
DELETE FROM tasks
WHERE done = 1;
```

Removes all completed tasks.

---

# 📚 What I Learned

- REST API fundamentals
- CRUD operations
- Flask routing
- SQLite database integration
- SQL queries
- Parameterized SQL statements
- HTTP methods (GET, POST, PUT, DELETE)
- HTTP status codes
- Persistent data storage
- API testing using Browser and cURL
- Version control with Git & GitHub

---

# 🎯 Learning Outcomes

By completing this project I learned how to:

- Design RESTful APIs
- Store data permanently using SQLite
- Connect Flask with a relational database
- Validate user input
- Return proper JSON responses
- Handle HTTP status codes correctly
- Execute SQL directly in SQLite
- Understand how APIs interact with databases

---

# 🚀 Future Improvements

- Authentication (JWT)
- User accounts
- Search tasks
- Task filtering
- Pagination
- Docker support
- Swagger/OpenAPI documentation
- Automated testing with Pytest
- Cloud deployment (Render / Railway)

---

# 👨‍💻 Author

**Mian Muhammad Hassan**

Backend Developer | Python Developer

📧 Email: your-email@example.com

💼 LinkedIn

```
https://linkedin.com/in/mianhasssan
```

🐙 GitHub

```
https://github.com/mianhasssan
```

---

# 📜 License

This project was created for educational purposes as part of the **FlyRank Backend Internship Program**.