# 🐍 Day 8 - Python Functions

# Introduction

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we create a function once and call it whenever required.

Functions make programs shorter, cleaner, reusable, and easier to understand.

---

# Advantages of Functions

- Reduce code repetition
- Improve code readability
- Easy to debug
- Easy to maintain
- Code reusability
- Modular programming

---

# Syntax

```python
def function_name():
    # code
```

Example

```python
def hello():
    print("Hello World")

hello()
```

Output

```
Hello World
```

---

# Components of Function

1. def Keyword
2. Function Name
3. Parentheses ()
4. Parameters (Optional)
5. Colon (:)
6. Function Body
7. Return Statement (Optional)

---

# Types of Functions

## 1. Built-in Functions

Functions already provided by Python.

Examples

```python
print()
input()
len()
max()
min()
sum()
type()
abs()
round()
```

Example

```python
numbers=[10,20,30]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
```

---

## 2. User Defined Functions

Functions created by the programmer.

Example

```python
def welcome():
    print("Welcome to Python")

welcome()
```

---

# Function Calling

A function executes only when it is called.

```python
def greet():
    print("Good Morning")

greet()
```

---

# Function with Parameters

Parameters receive values during function call.

```python
def greet(name):
    print("Hello",name)

greet("Pushpa")
```

Output

```
Hello Pushpa
```

---

# Multiple Parameters

```python
def add(a,b):
    print(a+b)

add(10,20)
```

Output

```
30
```

---

# Return Statement

The return keyword sends the result back to the caller.

```python
def square(n):
    return n*n

ans=square(5)

print(ans)
```

Output

```
25
```

---

# Function Without Return

```python
def display():
    print("Python")

display()
```

---

# Function Returning Multiple Values

```python
def calc(a,b):
    return a+b,a-b,a*b

x,y,z=calc(20,10)

print(x)
print(y)
print(z)
```

---

# Default Arguments

```python
def greet(name="Student"):
    print("Hello",name)

greet()
greet("Pushpa")
```

---

# Positional Arguments

```python
def student(name,age):
    print(name,age)

student("Pushpa",20)
```

---

# Keyword Arguments

```python
def student(name,age):
    print(name,age)

student(age=20,name="Pushpa")
```

---

# Variable Length Arguments

## *args

Accepts multiple values.

```python
def total(*numbers):
    print(sum(numbers))

total(10,20,30,40)
```

---

## **kwargs

Accepts key-value pairs.

```python
def info(**student):
    print(student)

info(name="Pushpa",age=20,city="Patna")
```

---

# Local Variable

A variable declared inside a function.

```python
def demo():
    x=10
    print(x)

demo()
```

---

# Global Variable

A variable declared outside a function.

```python
x=100

def demo():
    print(x)

demo()
```

---

# Lambda Function

A lambda function is an anonymous function.

```python
square=lambda x:x*x

print(square(6))
```

Output

```
36
```

---

# Recursive Function

A recursive function calls itself.

Example

```python
def factorial(n):

    if n==1:
        return 1

    return n*factorial(n-1)

print(factorial(5))
```

Output

```
120
```

---

# Nested Function

A function inside another function.

```python
def outer():

    def inner():
        print("Inside Inner Function")

    inner()

outer()
```

---

# pass Statement

Used to create an empty function.

```python
def demo():
    pass
```

---

# Docstring

Used to describe a function.

```python
def add(a,b):
    """
    Returns addition of two numbers.
    """
    return a+b
```

---

# Parameter vs Argument

Parameter → Variable in function definition.

Argument → Actual value passed during function call.

Example

```python
def add(a,b):
    return a+b

add(10,20)
```

Here

```
a,b → Parameters

10,20 → Arguments
```

---

# Summary

✔ Function

✔ Built-in Function

✔ User Defined Function

✔ Function Calling

✔ Parameters

✔ Arguments

✔ Return Statement

✔ Default Arguments

✔ Positional Arguments

✔ Keyword Arguments

✔ *args

✔ **kwargs

✔ Local Variable

✔ Global Variable

✔ Lambda Function

✔ Recursive Function

✔ Nested Function

✔ pass Statement

✔ Docstring

✔ Parameter vs Argument

---