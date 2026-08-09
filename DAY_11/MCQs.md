# Day 11 - Python Exception Handling MCQs

## 🟢 Basic Level

### 1. Which keyword is used to handle exceptions?

A. `error`  
B. `try`  
C. `catch`  
D. `handle`

**Answer:** B. `try`

---

### 2. Which keyword is used to handle an exception?

A. `except`  
B. `catch`  
C. `error`  
D. `finally`

**Answer:** A. `except`

---

### 3. Which block contains code that may cause an exception?

A. `except`  
B. `else`  
C. `try`  
D. `finally`

**Answer:** C. `try`

---

### 4. Which block executes when no exception occurs?

A. `except`  
B. `else`  
C. `finally`  
D. `raise`

**Answer:** B. `else`

---

### 5. Which block is normally executed whether an exception occurs or not?

A. `try`  
B. `except`  
C. `else`  
D. `finally`

**Answer:** D. `finally`

---

### 6. Which exception occurs when dividing by zero?

A. `ValueError`  
B. `TypeError`  
C. `ZeroDivisionError`  
D. `NameError`

**Answer:** C. `ZeroDivisionError`

---

### 7. Which exception occurs when converting invalid text into an integer?

```python
int("hello")
```

A. `TypeError`  
B. `ValueError`  
C. `KeyError`  
D. `IndexError`

**Answer:** B. `ValueError`

---

### 8. Which exception occurs when accessing an invalid list index?

A. `KeyError`  
B. `IndexError`  
C. `ValueError`  
D. `NameError`

**Answer:** B. `IndexError`

---

### 9. Which exception occurs when accessing a missing dictionary key?

A. `IndexError`  
B. `KeyError`  
C. `TypeError`  
D. `ValueError`

**Answer:** B. `KeyError`

---

### 10. Which keyword is used to manually raise an exception?

A. `throw`  
B. `error`  
C. `raise`  
D. `exception`

**Answer:** C. `raise`

---

# 🟡 Intermediate Level

### 11. What is the output?

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
```

A. `10`  
B. `0`  
C. `Error`  
D. Program crashes

**Answer:** C. `Error`

---

### 12. What is the output?

```python
try:
    x = int("10")
except ValueError:
    print("Invalid")
else:
    print("Valid")
```

A. `Invalid`  
B. `Valid`  
C. Error  
D. Nothing

**Answer:** B. `Valid`

---

### 13. What is the output?

```python
try:
    print("Hello")
finally:
    print("Python")
```

A. `Hello`  
B. `Python`  
C. Both `Hello` and `Python`  
D. Error

**Answer:** C. Both `Hello` and `Python`

---

### 14. What does `as e` allow us to access?

A. Variable name  
B. Exception object  
C. Function  
D. Class

**Answer:** B. Exception object

---

### 15. Which is a valid syntax?

A.

```python
try:
    print("Hello")
except:
    print("Error")
```

B.

```python
try
    print("Hello")
except:
    print("Error")
```

C.

```python
try:
print("Hello")
except:
print("Error")
```

D.

```python
try:
    print("Hello")
catch:
    print("Error")
```

**Answer:** A

---

### 16. What exception occurs here?

```python
numbers = [10, 20, 30]
print(numbers[5])
```

A. `ValueError`  
B. `KeyError`  
C. `IndexError`  
D. `TypeError`

**Answer:** C. `IndexError`

---

### 17. What exception occurs here?

```python
print("Python" + 10)
```

A. `ValueError`  
B. `TypeError`  
C. `IndexError`  
D. `KeyError`

**Answer:** B. `TypeError`

---

### 18. What exception occurs here?

```python
print(age)
```

when `age` has not been defined.

A. `NameError`  
B. `ValueError`  
C. `TypeError`  
D. `KeyError`

**Answer:** A. `NameError`

---

### 19. Which module is commonly used for creating abstract classes?

A. `math`  
B. `abc`  
C. `os`  
D. `random`

**Answer:** B. `abc`

---

### 20. Which class is commonly used as the base for abstract classes?

A. `Abstract`  
B. `ABC`  
C. `Exception`  
D. `BaseClass`

**Answer:** B. `ABC`

---

# 🔴 Advanced Level

### 21. Which decorator is used for abstract methods?

A. `@abstract`  
B. `@abstractmethod`  
C. `@method`  
D. `@abstract_class`

**Answer:** B. `@abstractmethod`

---

### 22. Which class should custom exceptions normally inherit from?

A. `Error`  
B. `Exception`  
C. `Object`  
D. `Base`

**Answer:** B. `Exception`

---

### 23. What is the purpose of a custom exception?

A. To create application-specific errors  
B. To create loops  
C. To create variables  
D. To create functions

**Answer:** A. To create application-specific errors

---

### 24. What happens if an exception is not handled?

A. Program normally continues  
B. Python automatically fixes it  
C. Program terminates with an error  
D. Nothing happens

**Answer:** C. Program terminates with an error

---

### 25. What is the output?

```python
try:
    x = 10
    y = 2
    print(x / y)

except ZeroDivisionError:
    print("Error")

else:
    print("Success")
```

A. `Error`  
B. `Success`  
C. `5` followed by `Success`  
D. `5`

**Answer:** C. `5` followed by `Success`

---

### 26. What is the output?

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Done")
```

A. `Cannot divide`  
B. `Done`  
C. Both `Cannot divide` and `Done`  
D. Error

**Answer:** C. Both `Cannot divide` and `Done`

---

### 27. Which order is correct?

A. `except → try → finally → else`  
B. `try → except → else → finally`  
C. `try → finally → except → else`  
D. `else → try → except → finally`

**Answer:** B. `try → except → else → finally`

---

### 28. Can one `try` block have multiple `except` blocks?

A. Yes  
B. No  
C. Only two  
D. Only three

**Answer:** A. Yes

---

### 29. Which approach is generally better?

A. Catch every error with an empty `except`
B. Catch specific exceptions when possible
C. Never handle exceptions
D. Use `print()` instead of exceptions

**Answer:** B. Catch specific exceptions when possible

---

### 30. What is the main purpose of exception handling?

A. Make code longer  
B. Handle runtime errors safely  
C. Remove variables  
D. Create classes

**Answer:** B. Handle runtime errors safely

---

# 🎯 Quick Revision

| Concept | Keyword / Exception |
|---|---|
| Start error handling | `try` |
| Handle error | `except` |
| No error | `else` |
| Cleanup/final code | `finally` |
| Manually raise error | `raise` |
| Invalid conversion | `ValueError` |
| Division by zero | `ZeroDivisionError` |
| Wrong data type operation | `TypeError` |
| Invalid list index | `IndexError` |
| Missing dictionary key | `KeyError` |
| Undefined variable | `NameError` |
| Missing file | `FileNotFoundError` |
| Custom error | `class MyError(Exception)` |

---

# 🏆 Day 11 MCQ Challenge

Score yourself:

- 25–30 = Excellent 🔥
- 20–24 = Very Good 💪
- 15–19 = Good 👍
- 10–14 = Need More Practice 📚
- Below 10 = Revise Exception Handling 🔄