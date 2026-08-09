# Day 10 - OOP Assignment

## Topic: Object-Oriented Programming in Python

---

# Part A: Theory Questions

1. What is OOP?

2. What is a class?

3. What is an object?

4. What is the difference between a class and an object?

5. What is `self`?

6. What is a constructor?

7. What is `__init__()`?

8. What is an instance variable?

9. What is a class variable?

10. What is an instance method?

11. What is a class method?

12. What is a static method?

13. What is encapsulation?

14. What is inheritance?

15. What is polymorphism?

16. What is abstraction?

17. What is method overriding?

18. What is method overloading in Python?

19. What is `super()`?

20. What are the four pillars of OOP?

---

# Part B: Basic Coding Questions

## 1. Student Class

Create a `Student` class with:

- Name
- Age
- Roll Number
- Marks

Create an object and display all details.

---

## 2. Rectangle Class

Create a `Rectangle` class with:

- Length
- Width

Calculate:

- Area
- Perimeter

---

## 3. Bank Account

Create a `BankAccount` class with:

- Account Holder
- Account Number
- Balance

Create methods:

- `deposit()`
- `withdraw()`
- `check_balance()`

---

## 4. Employee Class

Create an `Employee` class with:

- Name
- Employee ID
- Salary

Create a method to calculate annual salary.

---

## 5. Calculator Class

Create a `Calculator` class with methods:

- `add()`
- `subtract()`
- `multiply()`
- `divide()`

---

# Part C: Inheritance

## 6. Single Inheritance

Create:

```text
Animal
   ↓
Dog
```

Animal should have:

```text
eat()
```

Dog should have:

```text
bark()
```

---

## 7. Multilevel Inheritance

Create:

```text
Grandparent
     ↓
Parent
     ↓
Child
```

Each class should contain one method.

---

## 8. Multiple Inheritance

Create:

```text
Father       Mother
    \         /
       Child
```

The Child class should access methods from both parent classes.

---

## 9. Method Overriding

Create:

```text
Animal
   ↓
Dog
```

Both classes should have a `sound()` method.

Override the parent method inside the child class.

---

# Part D: Encapsulation

## 10. Private Variable

Create a `BankAccount` class with a private variable:

```python
__balance
```

Create methods:

```text
deposit()
withdraw()
get_balance()
```

---

## 11. Getter and Setter

Create a `Student` class with private marks.

Create:

```text
get_marks()
set_marks()
```

Use the setter to update marks and getter to display marks.

---

# Part E: Polymorphism

## 12. Shape Polymorphism

Create these classes:

```text
Circle
Rectangle
Triangle
```

Each class should contain:

```text
area()
```

Call the same `area()` method for different objects.

---

## 13. Animal Polymorphism

Create:

```text
Dog
Cat
Cow
```

Each class should contain:

```text
sound()
```

Call the same method for all objects.

---

# Part F: Abstraction

## 14. Abstract Vehicle

Create an abstract class:

```text
Vehicle
```

with an abstract method:

```text
start()
```

Create child classes:

```text
Car
Bike
```

Implement `start()` in both child classes.

Use:

```python
from abc import ABC, abstractmethod
```

---

# Part G: Real-World Project

## 15. Student Management System

Create a complete Student Management System using OOP.

### Features

```text
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Grade
7. Exit
```

### Requirements

Use:

- Classes
- Objects
- Constructor
- Methods
- Encapsulation
- Exception Handling
- List or Dictionary

---

# Bonus Challenge

## Bank Management System

Build a complete Bank Management System using:

- Class
- Object
- Constructor
- Encapsulation
- Inheritance
- Polymorphism
- Exception Handling

### Features

```text
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Account Details
6. Exit
```

---

# Submission Checklist

- [ ] Complete Theory Questions
- [ ] Complete Basic Programs
- [ ] Complete Inheritance Programs
- [ ] Complete Encapsulation Programs
- [ ] Complete Polymorphism Programs
- [ ] Complete Abstraction Program
- [ ] Build Student Management System
- [ ] Build Bank Management System

---

# Day 10 Goal

Don't just read OOP.

Learn → Practice → Code → Build → Improve

## Day 10 Status

OOP Assignment: Completed