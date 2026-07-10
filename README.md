# Tiny Backend API

A minimal Flask-based REST API demonstrating the fundamentals of backend development, HTTP request handling, and JSON responses. This project was built as a learning exercise to understand the request–response lifecycle and establish a professional GitHub workflow.

## Features

* Lightweight Flask server
* Two JSON API endpoints
* RESTful GET requests
* Clean and beginner-friendly codebase
* Ready for local development

## Tech Stack

* Python 3
* Flask

## Project Structure

```text
tiny-backend/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/tiny-backend.git
cd tiny-backend
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the development server

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### GET /

Returns a welcome message.

**Request**

```http
GET /
```

**Response**

```json
{
  "status": "success",
  "message": "Welcome to my Tiny Backend API"
}
```

---

### GET /hello

Returns a simple greeting.

**Request**

```http
GET /hello
```

**Response**

```json
{
  "message": "Hello, World!"
}
```

## Testing the API

### Using a Web Browser

Visit:

```text
http://127.0.0.1:5000/
```

or

```text
http://127.0.0.1:5000/hello
```

### Using curl

```bash
curl http://127.0.0.1:5000/
```

```bash
curl http://127.0.0.1:5000/hello
```

## Learning Objectives

This project demonstrates:

* Building a backend server with Flask
* Creating REST API endpoints
* Returning JSON responses
* Understanding the HTTP request–response cycle
* Testing APIs using both a browser and `curl`
* Managing a project with Git and GitHub

## Future Improvements

* Add POST endpoints
* Implement request validation
* Add error handling
* Introduce environment variables
* Write automated tests
* Deploy the API to a cloud platform (Render, Railway, or PythonAnywhere)


* GitHub: https://github.com/<mianhasssan>
* LinkedIn: https://www.linkedin.com/in/<mianhasssan>
