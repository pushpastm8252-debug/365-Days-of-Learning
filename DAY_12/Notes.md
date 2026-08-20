# 📘 Day 12 – Notes

## 1. What is a Web Framework?

A web framework provides tools and libraries that help developers build web applications and backend services.

Python has several web frameworks, including:

- Flask
- FastAPI
- Django

---

# 2. Flask

Flask is a lightweight and flexible Python web framework.

It is based on the WSGI standard and is commonly used to build web applications and REST APIs.

## Advantages

- Easy to learn
- Lightweight
- Flexible
- Large ecosystem
- Simple project structure

## Basic Flask Application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 3. FastAPI

FastAPI is a modern Python framework for building APIs.

It uses Python type hints for validation and generates interactive API documentation automatically.

## Advantages

- High performance
- Type hints
- Automatic validation
- Automatic API documentation
- Supports asynchronous programming

## Basic FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

---

# 4. Flask vs FastAPI

| Feature | Flask | FastAPI |
|---|---|---|
| Main Use | Web Apps & APIs | APIs |
| Performance | Good | High |
| Type Hints | Optional | Strongly Used |
| Validation | Manual/Extensions | Built-in |
| Documentation | Additional Setup | Automatic |
| Async | Supported | Strong Support |
| Flexibility | Very High | High |

---

# 5. REST API

REST means:

**Representational State Transfer**

REST is an architectural style for designing networked applications.

REST APIs commonly use HTTP methods to perform operations.

---

# 6. HTTP Methods

## GET

Used to retrieve data.

```text
GET /students
```

## POST

Used to create new data.

```text
POST /students
```

## PUT

Used to update existing data.

```text
PUT /students/1
```

## DELETE

Used to delete data.

```text
DELETE /students/1
```

---

# 7. API Endpoint

An endpoint is a specific URL where an API provides a resource or service.

Example:

```text
/students
/students/1
/products
/users
```

---

# 8. JSON

JSON stands for:

**JavaScript Object Notation**

It is commonly used for exchanging data between clients and servers.

Example:

```json
{
    "id": 1,
    "name": "Pushpa",
    "course": "CSE"
}
```

---

# 9. CRUD

CRUD represents four basic database operations.

| Operation | Meaning |
|---|---|
| Create | Add new data |
| Read | Retrieve data |
| Update | Modify data |
| Delete | Remove data |

---

# 10. Database Integration

Database integration means connecting a backend application to a database.

Popular databases include:

- SQLite
- MySQL
- PostgreSQL
- MongoDB

For learning and small applications, SQLite is very convenient because it stores the database in a local file.

---

# 11. SQLite

SQLite is a lightweight relational database.

Example:

```python
import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

connection.commit()
connection.close()
```

---

# 12. Client-Server Architecture

A basic backend application works like this:

```text
Client
   ↓
HTTP Request
   ↓
API
   ↓
Backend
   ↓
Database
   ↓
Backend
   ↓
HTTP Response
   ↓
Client
```

---

# 13. Flask API Example

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def students():
    data = [
        {"id": 1, "name": "Pushpa"},
        {"id": 2, "name": "Rahul"}
    ]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 14. FastAPI API Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def students():

    return [
        {"id": 1, "name": "Pushpa"},
        {"id": 2, "name": "Rahul"}
    ]
```

---

# 15. Important Terms

### Client

The application making a request.

### Server

The application processing the request.

### API

A communication interface between software applications.

### Endpoint

A specific API URL.

### Request

Information sent by the client.

### Response

Information returned by the server.

### Database

A system used to store and manage data.

---

# 🎯 Key Takeaway

Flask provides a flexible and lightweight way to build web applications and APIs.

FastAPI focuses strongly on modern API development, type hints, validation, and automatic documentation.

REST APIs allow clients and servers to communicate using HTTP, while database integration allows applications to store and manage persistent data.