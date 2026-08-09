# Day 11 - Exception Handling Practice Questions

## 🟢 Basic Level

### 1. Division Program

Take two numbers from the user and divide them.

Handle:

- `ValueError`
- `ZeroDivisionError`

---

### 2. Integer Input

Ask the user to enter an integer.

If the user enters invalid data, display:

```text
Please enter a valid integer.
```

---

### 3. List Index

Create a list:

```python
numbers = [10, 20, 30, 40, 50]
```

Ask the user for an index and display the element.

Handle `IndexError`.

---

### 4. Dictionary Key

Create:

```python
student = {
    "name": "Pushpa",
    "age": 20,
    "course": "CSE"
}
```

Ask the user for a key.

Handle `KeyError`.

---

### 5. Type Error

Create a program that tries to add a string and an integer.

Handle `TypeError`.

---

## 🟡 Intermediate Level

### 6. Calculator

Create a calculator using:

```text
+
-
*
/
```

Handle:

- `ValueError`
- `ZeroDivisionError`

---

### 7. Age Validation

Take age from the user.

If age is negative, raise:

```python
ValueError
```

---

### 8. Password Validation

Ask the user to enter a password.

If the password is incorrect, raise a custom exception.

---

### 9. Multiple Exceptions

Write a program that can handle:

```text
ValueError
TypeError
ZeroDivisionError
```

using multiple `except` blocks.

---

### 10. try-except-else

Write a program that takes two numbers and uses:

```text
try
except
else
```

to display the result.

---

### 11. try-except-finally

Write a program that demonstrates:

```text
try
except
finally
```

Print `"Program completed"` from the `finally` block.

---

### 12. Number Validation

Keep asking the user for a number until they enter a valid integer.

Use a `while` loop and exception handling.

---

### 13. Marks Validation

Take marks from the user.

Rules:

```text
0 <= marks <= 100
```

If marks are outside this range, raise an exception.

---

### 14. ATM Withdrawal

Create an ATM program.

If withdrawal amount is greater than balance:

```text
Insufficient balance
```

Handle the situation using exception handling.

---

### 15. File Handling

Try to open:

```text
data.txt
```

If the file does not exist, handle:

```python
FileNotFoundError
```

---

# 🔴 Advanced Level

### 16. Custom Exception

Create:

```python
class AgeError(Exception):
    pass
```

Raise this exception when age is less than 18.

---

### 17. Bank Account

Create a `BankAccount` class with:

```text
deposit()
withdraw()
check_balance()
```

Handle invalid withdrawal using exceptions.

---

### 18. Student Management

Create a Student class.

Validate:

- Name
- Age
- Marks

Use exception handling for invalid input.

---

### 19. Login System

Create a login system.

Features:

```text
Username
Password
Login
```

Create a custom exception for incorrect login details.

---

### 20. Shopping Cart

Create a shopping cart.

Handle:

- Invalid product price
- Invalid quantity
- Removing unavailable product

---

# 🔥 Challenge Questions

### 21. ATM System

Build a complete ATM system with:

```text
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit
```

Use exception handling throughout the program.

---

### 22. Quiz Application

Create a quiz program.

Handle invalid answers and invalid input.

---

### 23. Library Management System

Create a library system with:

```text
Add Book
Issue Book
Return Book
Search Book
```

Handle unavailable books using exceptions.

---

### 24. Employee Management System

Create an Employee class.

Raise an exception if salary is:

```text
less than 0
```

---

### 25. Complete Exception Handling Project

Create a menu-driven program containing:

```text
1. Calculator
2. Student Management
3. Bank Account
4. File Handling
5. Exit
```

Use proper exception handling for every operation.

---

# 🎯 Practice Checklist

- [ ] ValueError
- [ ] TypeError
- [ ] ZeroDivisionError
- [ ] IndexError
- [ ] KeyError
- [ ] NameError
- [ ] FileNotFoundError
- [ ] try
- [ ] except
- [ ] else
- [ ] finally
- [ ] raise
- [ ] Custom Exception
- [ ] Exception Handling in Functions
- [ ] Exception Handling in Classes

# 🚀 Goal

Practice every question by writing the code yourself.

**Don't just copy the solution — first try to solve it independently.**