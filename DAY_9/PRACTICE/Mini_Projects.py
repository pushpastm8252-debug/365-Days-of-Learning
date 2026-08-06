# ==============================
# MINI PROJECT 1: CALCULATOR
# ==============================

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n===== CALCULATOR =====")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter Choice: ")

    if choice == "5":
        break

    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    if choice == "1":
        print("Answer =", add(a, b))

    elif choice == "2":
        print("Answer =", sub(a, b))

    elif choice == "3":
        print("Answer =", mul(a, b))

    elif choice == "4":
        print("Answer =", div(a, b))

    else:
        print("Invalid Choice")


# ==============================
# MINI PROJECT 2: STUDENT RECORD
# ==============================

FILE = "students.txt"

def add_student():
    name = input("Name : ")
    roll = input("Roll : ")
    marks = input("Marks : ")

    with open(FILE, "a") as f:
        f.write(f"{name},{roll},{marks}\n")

def view_students():
    try:
        with open(FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No Records Found")

while True:

    print("\n===== STUDENT RECORD =====")
    print("1.Add Student")
    print("2.View Students")
    print("3.Exit")

    ch = input("Choice : ")

    if ch == "1":
        add_student()

    elif ch == "2":
        view_students()

    elif ch == "3":
        break

    else:
        print("Invalid Choice")


# ==============================
# MINI PROJECT 3: CONTACT BOOK
# ==============================

contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Display All")
    print("4.Delete Contact")
    print("5.Exit")

    ch = input("Enter Choice : ")

    if ch == "1":

        name = input("Name : ")
        phone = input("Phone : ")

        contacts[name] = phone

    elif ch == "2":

        name = input("Enter Name : ")

        if name in contacts:
            print(name, contacts[name])
        else:
            print("Not Found")

    elif ch == "3":

        for i in contacts:
            print(i, ":", contacts[i])

    elif ch == "4":

        name = input("Delete Name : ")

        if name in contacts:
            del contacts[name]

    elif ch == "5":
        break

    else:
        print("Invalid Choice")


# =========================================
# MINI PROJECT 4 : NOTES MANAGER
# =========================================

FILE = "notes.txt"

def add_note():
    note = input("Enter Note : ")
    with open(FILE, "a") as f:
        f.write(note + "\n")
    print("Note Saved Successfully.")

def view_notes():
    try:
        with open(FILE, "r") as f:
            print("\n----- YOUR NOTES -----")
            print(f.read())
    except FileNotFoundError:
        print("No Notes Found.")

while True:

    print("\n===== NOTES MANAGER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        add_note()

    elif ch == "2":
        view_notes()

    elif ch == "3":
        break

    else:
        print("Invalid Choice")


# =========================================
# MINI PROJECT 5 : QUIZ APPLICATION
# =========================================

questions = [
    ("Python is developed by?", "Guido van Rossum"),
    ("Keyword to create function?", "def"),
    ("Extension of Python File?", ".py"),
    ("Largest Planet?", "Jupiter"),
    ("Capital of India?", "Delhi")
]

score = 0

print("\n===== QUIZ APPLICATION =====")

for q, ans in questions:

    user = input(q + " : ")

    if user.lower() == ans.lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct Answer :", ans)

print("\nYour Score =", score, "/", len(questions))


# =========================================
# MINI PROJECT 6 : EXPENSE TRACKER
# =========================================

expenses = []

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":

        amount = float(input("Enter Amount : "))
        expenses.append(amount)

    elif ch == "2":

        print("\nExpenses")

        for i in expenses:
            print(i)

    elif ch == "3":

        print("Total Expense =", sum(expenses))

    elif ch == "4":
        break

    else:
        print("Invalid Choice")
        


# =========================================
# MINI PROJECT 7 : LOGIN & REGISTRATION SYSTEM
# =========================================

FILE = "users.txt"

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE, "a") as f:
        f.write(username + "," + password + "\n")

    print("Registration Successful!")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open(FILE, "r") as f:
            for line in f:
                u, p = line.strip().split(",")

                if username == u and password == p:
                    print("Login Successful!")
                    return

        print("Invalid Username or Password")

    except FileNotFoundError:
        print("No User Registered.")

while True:

    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    ch = input("Choice : ")

    if ch == "1":
        register()

    elif ch == "2":
        login()

    elif ch == "3":
        break

    else:
        print("Invalid Choice")


# =========================================
# MINI PROJECT 8 : LIBRARY MANAGEMENT SYSTEM
# =========================================

books = []

while True:

    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Display Books")
    print("4. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":

        book = input("Book Name : ")
        books.append(book)

    elif ch == "2":

        book = input("Issue Book : ")

        if book in books:
            books.remove(book)
            print("Book Issued Successfully")
        else:
            print("Book Not Available")

    elif ch == "3":

        print("\nAvailable Books")

        for b in books:
            print("-", b)

    elif ch == "4":
        break

    else:
        print("Invalid Choice")


# =========================================
# MINI PROJECT 9 : BANKING MANAGEMENT SYSTEM
# =========================================

balance = 0

while True:

    print("\n===== BANK SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":

        amount = float(input("Enter Amount : "))
        balance += amount

    elif ch == "2":

        amount = float(input("Enter Amount : "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif ch == "3":

        print("Current Balance =", balance)

    elif ch == "4":
        break

    else:
        print("Invalid Choice")


# =========================================
# MINI PROJECT 10 : MINI FILE EXPLORER
# =========================================

import os

while True:

    print("\n===== FILE EXPLORER =====")
    print("1. Show Files")
    print("2. Create File")
    print("3. Delete File")
    print("4. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":

        files = os.listdir()

        print("\nFiles & Folders")

        for file in files:
            print(file)

    elif ch == "2":

        name = input("Enter File Name : ")

        with open(name, "w") as f:
            f.write("New File Created Successfully")

        print("File Created")

    elif ch == "3":

        name = input("Enter File Name : ")

        if os.path.exists(name):
            os.remove(name)
            print("File Deleted Successfully")
        else:
            print("File Not Found")

    elif ch == "4":
        break

    else:
        print("Invalid Choice")        