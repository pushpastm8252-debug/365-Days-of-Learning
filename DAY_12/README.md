# 🚀 Day 12 – Flask, FastAPI, REST API & Database Integration

Welcome to **Day 12** of my 365 Days of Python Learning Journey.

Today I explored the fundamentals of Python backend development and learned how Python frameworks can be used to build web applications and REST APIs.

## 📚 Topics Covered

- Python Web Frameworks
- Flask
- FastAPI
- Flask vs FastAPI
- REST API
- HTTP Methods
- API Endpoints
- JSON
- CRUD Operations
- Database Integration
- SQLite
- Client-Server Architecture
- Basic API Development

## 🎯 Learning Objective

The main objective of Day 12 was to understand how Python can be used for backend development.

I learned how:

```text
Client
   ↓
REST API
   ↓
Backend Framework
   ↓
Database
```

## 🐍 Flask

Flask is a lightweight Python web framework used for building web applications and APIs.

### Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

## ⚡ FastAPI

FastAPI is a modern Python framework designed mainly for building APIs.

### Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}
```

## ⚔️ Flask vs FastAPI

| Feature | Flask | FastAPI |
|---|---|---|
| Type | Web Framework | API Framework |
| Performance | Good | High |
| Learning | Easy | Easy to Moderate |
| Type Hints | Optional | Strongly Used |
| Validation | Extensions/Manual | Built-in |
| API Documentation | Additional Setup | Automatic |
| Async Support | Available | Excellent |
| Best For | Web Apps & APIs | APIs & Modern Backends |

## 🌐 REST API

REST stands for **Representational State Transfer**.

A REST API allows different applications to communicate using HTTP.

### Common HTTP Methods

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |

## 🗄️ Database Integration

A backend application can connect to a database to store and manage information.

For Day 12, I practiced with SQLite.

### Basic Architecture

```text
Frontend
   ↓
REST API
   ↓
Flask / FastAPI
   ↓
Database
```

## 🔄 CRUD Operations

CRUD means:

- Create
- Read
- Update
- Delete

## 💻 Mini Projects

- Flask Hello World API
- FastAPI Hello World API
- Student REST API
- SQLite Student Database
- CRUD API
- Task Management API

## 🎯 Learning Outcomes

After completing Day 12, I can:

- Explain Flask
- Explain FastAPI
- Compare Flask and FastAPI
- Understand REST APIs
- Understand HTTP methods
- Create basic API endpoints
- Work with JSON
- Understand CRUD operations
- Understand database integration
- Build basic backend applications

## 📂 Project Structure

```text
Day-12/
├── README.md
├── Notes.md
├── Practice_Questions.md
├── MCQs.md
├── Interview_Questions.md
├── Mini_Projects.md
├── Mini_Projects.py
├── Assignment.md
└── Reflection.md
```

## 🚀 Day 12 Completed Successfully!

**Learn → Practice → Code → Build → Improve**

### Author

**Pushpa Kumari**

B.Tech CSE | Python & AI/ML Learner

#Python #Flask #FastAPI #RESTAPI #BackendDevelopment #Database #PythonLearning