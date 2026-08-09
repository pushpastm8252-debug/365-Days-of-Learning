# Day 11 - Python Exception Handling Interview Questions

## 🟢 Basic Level

### 1. What is an exception in Python?

### 2. What is exception handling?

### 3. Why is exception handling important?

### 4. What is the difference between an error and an exception?

### 5. What is a SyntaxError?

### 6. What is a runtime exception?

### 7. What is the purpose of the `try` block?

### 8. What is the purpose of the `except` block?

### 9. What is the purpose of the `else` block?

### 10. What is the purpose of the `finally` block?

### 11. Can we use `try` without `except`?

### 12. Can we use multiple `except` blocks?

### 13. What is `Exception` in Python?

### 14. What is `raise`?

### 15. What is a custom exception?

---

# 🟡 Intermediate Level

### 16. What is the difference between `try-except` and `try-finally`?

### 17. What happens if an exception is not handled?

### 18. What happens when an exception occurs inside a `try` block?

### 19. Can `finally` execute when an exception occurs?

### 20. When should we use `else` with `try-except`?

### 21. What is `Exception as e`?

### 22. How do you handle multiple exceptions?

### 23. What is `ValueError`?

### 24. What is `TypeError`?

### 25. What is `ZeroDivisionError`?

### 26. What is `IndexError`?

### 27. What is `KeyError`?

### 28. What is `NameError`?

### 29. What is `FileNotFoundError`?

### 30. What is the difference between `ValueError` and `TypeError`?

---

# 🔴 Advanced Level

### 31. How do you create a custom exception?

### 32. Why should custom exceptions inherit from `Exception`?

### 33. What is exception propagation?

### 34. How does Python search for an exception handler?

### 35. What is exception chaining?

### 36. What is the difference between `raise` and `return`?

### 37. Can we raise an exception without handling it?

### 38. What is the purpose of `finally` in resource management?

### 39. Why should we avoid using a bare `except` unnecessarily?

### 40. Why is catching specific exceptions better than catching `Exception` everywhere?

### 41. Can exceptions be handled inside functions?

### 42. Can exceptions be handled inside class methods?

### 43. Can a custom exception contain additional information?

### 44. What happens if an exception occurs inside an `except` block?

### 45. What happens if an exception occurs inside a `finally` block?

---

# 💻 Coding Interview Questions

### 46. Write a program to safely divide two numbers.

### 47. Write a program to handle invalid integer input.

### 48. Write a program to handle division by zero.

### 49. Write a program to handle invalid list indexes.

### 50. Write a program to handle missing dictionary keys.

### 51. Write a calculator using exception handling.

### 52. Write a program that keeps asking for input until the user enters a valid number.

### 53. Create a custom `AgeError` exception.

### 54. Create a `BankAccount` class and handle insufficient balance using an exception.

### 55. Create a file-reading program that handles `FileNotFoundError`.

---

# ⭐ Important Interview Question

## Explain the complete flow of exception handling.

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)

finally:
    print("Program completed.")
```

### Flow:

```text
try
 ↓
Exception?
 ↓
YES → except
 ↓
NO → else
 ↓
finally
 ↓
Program continues
```

---

# 🎯 Most Important Questions to Prepare

1. What is exception handling?
2. Difference between error and exception.
3. Explain `try`, `except`, `else`, and `finally`.
4. What is `raise`?
5. What is a custom exception?
6. Explain `ValueError`.
7. Explain `TypeError`.
8. Explain `ZeroDivisionError`.
9. Explain `IndexError`.
10. Explain `KeyError`.
11. What is `Exception as e`?
12. Why should specific exceptions be handled?
13. How do you create a custom exception?
14. What happens when an exception is not handled?
15. Explain exception handling with a real-world example.

---

# 🏆 Interview Tip

Don't only memorize definitions.

For every exception-handling concept, practice writing a small program.

**Understand → Code → Debug → Explain**
