# Day 11 - Exception Handling Assignment

## Topic: Exception Handling in Python

---

# Part A: Theory Questions

1. What is an exception?

2. What is exception handling?

3. Why do we use exception handling?

4. What is the difference between SyntaxError and an exception?

5. What is the purpose of `try`?

6. What is the purpose of `except`?

7. What is the purpose of `else`?

8. What is the purpose of `finally`?

9. What is the purpose of `raise`?

10. What is a custom exception?

11. What is `ValueError`?

12. What is `TypeError`?

13. What is `ZeroDivisionError`?

14. What is `IndexError`?

15. What is `KeyError`?

16. What is `NameError`?

17. What is `FileNotFoundError`?

18. What is `Exception as e`?

19. Why should we handle specific exceptions?

20. What happens when an exception is not handled?

---

# Part B: Basic Coding Questions

## 1. Safe Division

Write a program that takes two numbers and divides them.

Handle:

- `ValueError`
- `ZeroDivisionError`

---

## 2. Valid Integer

Take an integer from the user.

If the input is invalid, display:

```text
Please enter a valid integer.
```

---

## 3. List Index Handling

Create:

```python
numbers = [10, 20, 30, 40, 50]
```

Ask the user for an index.

Handle `IndexError`.

---

## 4. Dictionary Key Handling

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

## 5. Type Error Handling

Write a program that attempts to add a string and an integer.

Handle `TypeError`.

---

# Part C: try-except-else-finally

## 6. try-except

Write a program using:

```text
try
except
```

---

## 7. try-except-else

Write a program using:

```text
try
except
else
```

Display the result in the `else` block if no exception occurs.

---

## 8. try-except-finally

Write a program using:

```text
try
except
finally
```

Print:

```text
Program completed
```

from the `finally` block.

---

## 9. Complete Exception Handling

Create a program using:

```text
try
except
else
finally
```

Take two numbers and perform division.

---

# Part D: raise

## 10. Age Validation

Take age from the user.

If age is less than 0, raise:

```python
ValueError
```

---

## 11. Marks Validation

Take marks from the user.

Valid marks:

```text
0 to 100
```

If marks are outside the range, raise an exception.

---

## 12. Salary Validation

Take salary from the user.

If salary is negative, raise:

```python
ValueError
```

---

# Part E: Custom Exceptions

## 13. AgeError

Create:

```python
class AgeError(Exception):
    pass
```

Raise the exception if age is less than 18.

---

## 14. BalanceError

Create a custom exception:

```python
class BalanceError(Exception):
    pass
```

Use it when a user tries to withdraw more money than the available balance.

---

## 15. InvalidMarksError

Create:

```python
class InvalidMarksError(Exception):
    pass
```

Raise it when marks are below 0 or above 100.

---

# Part F: OOP + Exception Handling

## 16. Bank Account

Create a `BankAccount` class.

Methods:

```text
deposit()
withdraw()
check_balance()
```

Handle:

- Negative deposit
- Negative withdrawal
- Insufficient balance
- Invalid input

---

## 17. Student Management

Create a `Student` class.

Validate:

- Name
- Age
- Marks

Use exception handling for invalid values.

---

## 18. ATM System

Create an ATM using OOP.

Features:

```text
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

Handle all invalid inputs.

---

## 19. Library Management

Create a library system.

Features:

```text
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Search Book
```

Handle unavailable books using exceptions.

---

## 20. Shopping Cart

Create a shopping cart.

Features:

```text
1. Add Product
2. Remove Product
3. View Cart
4. Calculate Total
5. Exit
```

Handle invalid price, quantity, and unavailable products.

---

# 🔥 Final Challenge

## Bank Management System

Build a complete Bank Management System.

### Features

```text
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Account Details
6. Exit
```

### Requirements

Use:

- Classes
- Objects
- Constructor
- Encapsulation
- Methods
- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom Exceptions

---

# 🎯 Submission Checklist

- [ ] Complete Theory Questions
- [ ] Complete Basic Programs
- [ ] Practice `try`
- [ ] Practice `except`
- [ ] Practice `else`
- [ ] Practice `finally`
- [ ] Practice `raise`
- [ ] Create Custom Exception
- [ ] Practice OOP + Exception Handling
- [ ] Complete Bank Management System

---

# 🏆 Day 11 Goal

By the end of Day 11, I should be able to:

- Understand exceptions
- Handle runtime errors
- Validate user input
- Create custom exceptions
- Use `raise`
- Handle file errors
- Combine OOP with exception handling
- Build reliable Python applications

---

# 🚀 Motto

**Errors are not the end of the program.  
They are an opportunity to make the program better.**

Learn → Practice → Debug → Handle → Build