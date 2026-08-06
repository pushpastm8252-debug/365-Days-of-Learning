# 🐍 Day 9 - Modules, Packages, File Handling & Exception Handling

# 📦 What is a Module?

A module is a Python file (.py) that contains functions, variables, classes, and statements. Modules help organize code into separate files and promote code reusability.

Example:

```python
# math_operations.py

def add(a, b):
    return a + b
```

Using the module:

```python
import math_operations

print(math_operations.add(10, 20))
```

Output

```
30
```

---

# Why Use Modules?

- Code Reusability
- Better Code Organization
- Easy Maintenance
- Modular Programming
- Avoid Code Duplication

---

# Types of Modules

## 1. Built-in Modules

Modules already provided by Python.

Examples

```python
math
random
datetime
os
sys
time
calendar
statistics
```

Example

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

## 2. User-Defined Modules

Modules created by the programmer.

Example

```python
# calculator.py

def add(a, b):
    return a + b
```

Main File

```python
import calculator

print(calculator.add(10,20))
```

---

# Importing Modules

## import

```python
import math

print(math.factorial(5))
```

---

## from...import

```python
from math import sqrt

print(sqrt(49))
```

---

## import as

```python
import math as m

print(m.pi)
```

---

## Import Everything

```python
from math import *

print(sqrt(81))
print(pi)
```

---

# dir() Function

Displays all functions and variables available in a module.

```python
import math

print(dir(math))
```

---

# __name__ Variable

```python
print(__name__)
```

Output

```
__main__
```

---

# Creating Your Own Module

File: message.py

```python
def welcome():
    print("Welcome to Python")
```

Main File

```python
import message

message.welcome()
```

---

# 📁 What is a Package?

A package is a collection of multiple Python modules stored inside a folder.

Example

```
calculator/
│── __init__.py
│── add.py
│── sub.py
│── mul.py
```

---

# Why Use Packages?

- Organize Large Projects
- Group Related Modules
- Better Code Management

---

# __init__.py

The `__init__.py` file tells Python that a folder should be treated as a package.

Example

```
mypackage/
│── __init__.py
│── demo.py
```

---

# Importing Package

```python
from calculator import add
```

---

# Difference Between Module and Package

| Module | Package |
|---------|----------|
| Single .py File | Collection of Modules |
| Small Program | Large Project |
| Contains Functions | Contains Modules |

---

# 📄 File Handling

File handling is used to create, read, write, update, and delete files.

---

# open() Function

Syntax

```python
file = open("data.txt", "r")
```

---

# File Modes

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create New File |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

# Reading a File

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

---

# Reading One Line

```python
file = open("data.txt", "r")

print(file.readline())

file.close()
```

---

# Reading All Lines

```python
file = open("data.txt", "r")

print(file.readlines())

file.close()
```

---

# Writing to a File

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

---

# Appending Data

```python
file = open("data.txt", "a")

file.write("\nWelcome")

file.close()
```

---

# with Statement

Automatically closes the file.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

# seek()

Moves the file pointer.

```python
file = open("data.txt", "r")

file.seek(5)

print(file.read())
```

---

# tell()

Returns current file pointer position.

```python
file = open("data.txt", "r")

print(file.tell())
```

---

# ⚠️ Exception Handling

Exception handling prevents program crashes caused by runtime errors.

---

# Common Exceptions

- ZeroDivisionError
- ValueError
- TypeError
- NameError
- IndexError
- KeyError
- FileNotFoundError

---

# try

```python
try:
    print(10/0)
except:
    print("Error")
```

Output

```
Error
```

---

# try-except

```python
try:
    num = int(input("Enter Number: "))
except ValueError:
    print("Invalid Input")
```

---

# try-except-else

```python
try:
    a = 10
    b = 2
    print(a/b)

except:
    print("Error")

else:
    print("Division Successful")
```

---

# finally

```python
try:
    print(10/2)

finally:
    print("Program Finished")
```

---

# Multiple Exceptions

```python
try:
    x = int(input())
    print(10/x)

except ZeroDivisionError:
    print("Cannot Divide by Zero")

except ValueError:
    print("Invalid Input")
```

---

# raise Keyword

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# User-Defined Exception

```python
class InvalidAge(Exception):
    pass

age = -5

if age < 0:
    raise InvalidAge("Invalid Age")
```

---

# Summary

✅ Module

✅ Built-in Module

✅ User-defined Module

✅ import Statement

✅ from...import

✅ import as

✅ dir()

✅ __name__

✅ Package

✅ __init__.py

✅ File Handling

✅ File Modes

✅ open()

✅ read()

✅ readline()

✅ readlines()

✅ write()

✅ append()

✅ seek()

✅ tell()

✅ with Statement

✅ Exception Handling

✅ try

✅ except

✅ else

✅ finally

✅ raise

✅ Multiple Exceptions

✅ User-defined Exceptions

---