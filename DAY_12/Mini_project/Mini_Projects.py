# ============================================================
# DAY 12 - FLASK, FASTAPI, REST API & DATABASE PROJECTS
# ============================================================

# Install required packages:
#
# pip install flask fastapi uvicorn
#
# ============================================================


# ============================================================
# PROJECT 1: FLASK HELLO WORLD
# ============================================================

from flask import Flask, jsonify

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_home():
    return "Hello from Flask!"


@flask_app.route("/students")
def flask_students():

    students = [
        {"id": 1, "name": "Pushpa", "course": "CSE"},
        {"id": 2, "name": "Rahul", "course": "CSE"}
    ]

    return jsonify(students)


# Run Flask:
#
# flask_app.run(debug=True)


# ============================================================
# PROJECT 2: FASTAPI
# ============================================================

from fastapi import FastAPI

fastapi_app = FastAPI()


@fastapi_app.get("/")
def fastapi_home():

    return {
        "message": "Hello from FastAPI!"
    }


@fastapi_app.get("/students")
def get_students():

    return [
        {
            "id": 1,
            "name": "Pushpa",
            "course": "CSE"
        },
        {
            "id": 2,
            "name": "Rahul",
            "course": "CSE"
        }
    ]


# Run FastAPI:
#
# uvicorn Mini_Projects:fastapi_app --reload


# ============================================================
# PROJECT 3: SQLITE DATABASE
# ============================================================

import sqlite3


def create_database():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            age INTEGER
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully.")


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    name = input("Enter student name: ")
    course = input("Enter course: ")

    try:
        age = int(input("Enter age: "))

        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO students (name, course, age)
            VALUES (?, ?, ?)
            """,
            (name, course, age)
        )

        connection.commit()
        connection.close()

        print("Student added successfully.")

    except ValueError:
        print("Age must be a number.")


# ============================================================
# VIEW STUDENTS
# ============================================================

def view_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Course: {student[2]}, "
            f"Age: {student[3]}"
        )


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    try:

        student_id = int(input("Enter student ID: "))
        new_name = input("Enter new name: ")
        new_course = input("Enter new course: ")
        new_age = int(input("Enter new age: "))

        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE students
            SET name = ?, course = ?, age = ?
            WHERE id = ?
            """,
            (new_name, new_course, new_age, student_id)
        )

        connection.commit()
        connection.close()

        print("Student updated successfully.")

    except ValueError:
        print("Please enter valid values.")


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    try:

        student_id = int(input("Enter student ID: "))

        connection = sqlite3.connect("students.db")

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        connection.close()

        print("Student deleted successfully.")

    except ValueError:
        print("Invalid student ID.")


# ============================================================
# STUDENT MANAGEMENT MENU
# ============================================================

def student_management():

    create_database()

    while True:

        print("""
========================================
       STUDENT MANAGEMENT SYSTEM
========================================

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("Day 12 Mini Projects")
    print("Flask + FastAPI + REST API + SQLite")

    print("""
Available:

1. Run Student Management System

Flask and FastAPI applications are defined above
and can be run separately.
""")

    choice = input("Enter 1 to run Student Management System: ")

    if choice == "1":
        student_management()

    else:
        print("Thank you!")