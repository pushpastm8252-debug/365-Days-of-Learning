# Day 11 - Python Exception Handling

## 📚 Topic: Exception Handling in Python

Exception Handling ka use program me aane wali errors ko handle karne ke liye kiya jata hai, taaki program suddenly crash na ho.

---

# 1. What is an Exception?

Exception ek runtime error hota hai jo program ke execution ke time occur hota hai.

Example:

```python
a = 10
b = 0

print(a / b)
```

Output:

```text
ZeroDivisionError: division by zero
```

Agar exception handle nahi ki gayi, to program stop ho jayega.

---

# 2. Why Use Exception Handling?

Exception Handling ka use:

- Program ko crash hone se bachane ke liye
- Errors ko properly handle karne ke liye
- User ko meaningful message dene ke liye
- Program ko continue karne ke liye
- Reliable applications banane ke liye

---

# 3. Syntax Error vs Exception

## Syntax Error

Syntax rules galat hone par Syntax Error aata hai.

Example:

```python
if 10 > 5
    print("Yes")
```

Yahan `:` missing hai.

---

## Exception

Program syntactically correct hai, lekin execution ke time error aata hai.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

# 4. try Block

`try` block me woh code likhte hain jahan exception aa sakti hai.

Syntax:

```python
try:
    # risky code
```

Example:

```python
try:
    number = int(input("Enter number: "))
    print(number)
```

---

# 5. except Block

`except` block exception ko handle karta hai.

Example:

```python
try:
    number = int(input("Enter number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")
```

Agar user:

```text
abc
```

enter karta hai, program error show karne ke bajay message print karega.

---

# 6. try-except Example

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter numbers only.")
```

---

# 7. Multiple except Blocks

Ek `try` block ke saath multiple `except` blocks use kar sakte hain.

Example:

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 8. Exception as e

Exception ki actual information dekhne ke liye `as e` use kar sakte hain.

Example:

```python
try:
    print(10 / 0)

except Exception as e:
    print("Error:", e)
```

Output:

```text
Error: division by zero
```

---

# 9. Generic Exception

`Exception` ek broad base exception class hai.

Example:

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)

except Exception as e:
    print("Something went wrong:", e)
```

Specific exceptions ko prefer karna generally better hota hai.

---

# 10. else Block

`else` tab execute hota hai jab `try` block me koi exception nahi aati.

Syntax:

```python
try:
    # code

except:
    # error handling

else:
    # successful execution
```

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)
```

---

# 11. finally Block

`finally` block normally execute hota hai whether exception aaye ya na aaye.

Example:

```python
try:
    number = int(input("Enter number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")
```

---

# 12. try-except-else-finally

Complete structure:

```python
try:
    # risky code

except:
    # error handling

else:
    # if no error

finally:
    # always runs
```

Example:

```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    result = a / b

except ValueError:
    print("Enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Execution completed.")
```

---

# 13. Common Python Exceptions

## 1. ValueError

Wrong value type conversion.

```python
number = int("hello")
```

---

## 2. ZeroDivisionError

Zero se division.

```python
10 / 0
```

---

## 3. TypeError

Incompatible data types.

```python
print("10" + 5)
```

---

## 4. IndexError

Invalid list index.

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

## 5. KeyError

Dictionary me unavailable key access karna.

```python
student = {
    "name": "Pushpa"
}

print(student["age"])
```

---

## 6. NameError

Undefined variable use karna.

```python
print(age)
```

---

## 7. AttributeError

Object me unavailable attribute/method access karna.

Example:

```python
numbers = [1, 2, 3]

numbers.upper()
```

---

## 8. FileNotFoundError

Non-existing file open karne par.

```python
file = open("abc.txt")
```

---

# 14. Handling ValueError

```python
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid integer.")
```

---

# 15. Handling ZeroDivisionError

```python
try:
    a = 10
    b = int(input("Enter divisor: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 16. Handling IndexError

```python
numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Enter a valid index.")
```

---

# 17. Handling KeyError

```python
student = {
    "name": "Pushpa",
    "age": 20
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key does not exist.")
```

---

# 18. Handling TypeError

```python
try:
    result = "Python" + 10
    print(result)

except TypeError:
    print("Cannot combine these data types.")
```

---

# 19. Raising an Exception

Python me manually exception raise karne ke liye `raise` keyword use karte hain.

Example:

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Age:", age)
```

---

# 20. Custom Exception

Hum apni custom exception class bhi create kar sakte hain.

Example:

```python
class AgeError(Exception):
    pass


age = int(input("Enter age: "))

try:

    if age < 18:
        raise AgeError("Age must be 18 or above.")

    print("Eligible.")

except AgeError as e:
    print("Error:", e)
```

---

# 21. Exception Handling in Functions

Example:

```python
def divide(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))
```

---

# 22. Exception Handling with User Input

Example:

```python
while True:

    try:
        number = int(input("Enter a number: "))
        print("Number:", number)
        break

    except ValueError:
        print("Invalid input. Try again.")
```

---

# 23. Exception Handling with File Handling

```python
try:

    file = open("data.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:
    print("File not found.")
```

---

# 24. Better File Handling

`with` statement automatically manages the file resource.

```python
try:

    with open("data.txt", "r") as file:
        content = file.read()

        print(content)

except FileNotFoundError:
    print("File not found.")
```

---

# 25. Nested try

A `try` block can be inside another `try` block.

Example:

```python
try:

    number = int(input("Enter number: "))

    try:
        result = 10 / number
        print(result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print("Invalid number.")
```

---

# 26. Exception Handling in OOP

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        try:

            if amount > self.balance:
                raise ValueError("Insufficient balance.")

            self.balance -= amount

            print("Withdrawal successful.")
            print("Balance:", self.balance)

        except ValueError as e:
            print("Error:", e)


account = BankAccount(5000)

account.withdraw(2000)
account.withdraw(6000)
```

---

# 27. Important Rules

### Rule 1

Risky code should be inside `try`.

### Rule 2

Handle specific exceptions whenever possible.

### Rule 3

Do not use empty `except` unnecessarily.

### Rule 4

Use `finally` for cleanup tasks.

### Rule 5

Use `raise` when you want to create an exception intentionally.

### Rule 6

Use custom exceptions for application-specific errors.

---

# 28. Difference Between except and finally

| except | finally |
|---|---|
| Handles exceptions | Executes cleanup/final code |
| Runs when matching exception occurs | Normally runs whether exception occurs or not |
| Used for error handling | Used for cleanup |

---

# 29. Difference Between else and finally

| else | finally |
|---|---|
| Runs when no exception occurs | Normally runs in either case |
| Used after successful try | Used for final/cleanup operations |

---

# 30. Exception Handling Flow

```text
        try
         |
         v
   Exception occurs?
      /        \
    YES         NO
     |           |
     v           v
  except       else
     \           /
      \         /
       v       v
        finally
           |
           v
        Program
```

---

# 31. Real-World Example: Calculator

```python
def calculator():

    try:

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            print("Result:", a + b)

        elif operator == "-":
            print("Result:", a - b)

        elif operator == "*":
            print("Result:", a * b)

        elif operator == "/":

            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            print("Result:", a / b)

        else:
            print("Invalid operator.")

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError as e:
        print("Error:", e)


calculator()
```

---

# 32. Real-World Example: Age Validation

```python
try:

    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError as e:

    print("Error:", e)
```

---

# 33. Real-World Example: Login System

```python
correct_password = "python123"

try:

    password = input("Enter password: ")

    if password != correct_password:
        raise ValueError("Incorrect password.")

    print("Login successful.")

except ValueError as e:
    print("Login failed:", e)
```

---

# 34. Important Syntax

## Basic

```python
try:
    pass

except:
    pass
```

## Specific Exception

```python
try:
    pass

except ValueError:
    pass
```

## Multiple Exceptions

```python
try:
    pass

except ValueError:
    pass

except TypeError:
    pass
```

## With else

```python
try:
    pass

except ValueError:
    pass

else:
    pass
```

## With finally

```python
try:
    pass

except ValueError:
    pass

finally:
    pass
```

## Complete

```python
try:
    pass

except ValueError:
    pass

else:
    pass

finally:
    pass
```

---

# 35. Key Takeaways

- Exception is a runtime error.
- `try` contains risky code.
- `except` handles exceptions.
- `else` runs when no exception occurs.
- `finally` normally runs regardless of success or failure.
- `raise` manually raises an exception.
- Custom exceptions can be created using classes.
- Specific exceptions are usually better than a broad `Exception`.
- Exception handling makes programs more reliable.

---

# 🎯 Day 11 Learning Checklist

- [ ] Understand Exception
- [ ] Understand Syntax Error
- [ ] Learn try
- [ ] Learn except
- [ ] Learn else
- [ ] Learn finally
- [ ] Learn `Exception as e`
- [ ] Practice ValueError
- [ ] Practice TypeError
- [ ] Practice ZeroDivisionError
- [ ] Practice IndexError
- [ ] Practice KeyError
- [ ] Practice NameError
- [ ] Learn raise
- [ ] Create Custom Exception
- [ ] Practice Exception Handling in Functions
- [ ] Practice Exception Handling in OOP

---

# 🚀 Day 11 Goal

Learn how to handle errors properly and build programs that do not stop unexpectedly when users provide invalid input.

**Learn → Practice → Handle Errors → Build Reliable Programs**