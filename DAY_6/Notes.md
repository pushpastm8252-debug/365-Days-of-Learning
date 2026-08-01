# 📚 Day 6 - Python Functions

# 🐍 Python Functions

---

# 📌 What is a Function?

A function is a block of reusable code that performs a specific task.

Instead of writing the same code again and again, we create a function once and call it whenever needed.

Functions make programs clean, organized, and reusable.

---

# 📌 Why Do We Use Functions?

Functions help us to:

✅ Reduce code repetition

✅ Make code reusable

✅ Improve readability

✅ Divide large programs into smaller parts

✅ Make debugging easier

✅ Save development time

---

# 📌 Advantages of Functions

✔ Reusability

✔ Better Code Organization

✔ Easy Maintenance

✔ Easy Testing

✔ Better Readability

✔ Modular Programming

---

# 📌 Function Syntax

A function is defined using the **def** keyword.

General Syntax

def function_name(parameters):
    statements

Calling a Function

function_name()

---

# 📌 Function Naming Rules

✔ Function names should be meaningful.

✔ Use lowercase letters.

✔ Words should be separated using underscore (_).

Example:

calculate_sum()

student_details()

---

# 📌 Types of Functions

Python has two main types of functions.

## 1. Built-in Functions

These functions are already available in Python.

Examples

print()

input()

len()

type()

max()

min()

sum()

round()

sorted()

abs()

---

## 2. User-defined Functions

Functions created by the programmer are called user-defined functions.

Example:

Greeting Function

Calculator Function

Factorial Function

Prime Number Function

---

# 📌 Parameters

Parameters are variables written inside the function definition.

Example

def add(a, b):

Here,

a and b are parameters.

---

# 📌 Arguments

Arguments are actual values passed while calling a function.

Example

add(10,20)

Here,

10 and 20 are arguments.

---

# 📌 Types of Arguments

## 1. Positional Arguments

Arguments are passed in order.

Example

add(5,10)

---

## 2. Keyword Arguments

Arguments are passed using parameter names.

Example

add(a=5,b=10)

---

## 3. Default Arguments

A parameter has a default value.

Example

def greet(name="Guest")

If no value is passed,

Guest is used.

---

## 4. Variable Length Arguments

*args

Accepts multiple values.

---

## 5. Keyword Variable Arguments

**kwargs

Accepts multiple keyword values.

---

# 📌 Return Statement

The return keyword sends a value back from a function.

Example

return result

A function can return

✔ Integer

✔ Float

✔ String

✔ Boolean

✔ List

✔ Dictionary

---

# 📌 Difference Between print() and return

print()

✔ Displays output

✔ Cannot reuse output easily

return

✔ Sends output back

✔ Can be stored in variables

✔ Can be reused

---

# 📌 Local Variable

A variable created inside a function.

It can only be used inside that function.

---

# 📌 Global Variable

A variable created outside all functions.

It can be accessed from anywhere in the program.

---

# 📌 Scope

Scope means the area where a variable can be accessed.

Two types

✔ Local Scope

✔ Global Scope

---

# 📌 Lambda Function

A lambda function is a small anonymous function.

It is written in one line.

Used for short operations.

---

# 📌 Recursion

Recursion means a function calling itself.

Every recursive function must have

✔ Base Case

✔ Recursive Case

Without a base case,

the recursion never stops.

---

# 📌 Real-Life Applications of Functions

✔ ATM Machine

✔ Banking Software

✔ Calculator

✔ Games

✔ E-commerce Website

✔ Mobile Apps

✔ Machine Learning

✔ Artificial Intelligence

✔ Data Science

✔ Automation

---

# 📌 Best Practices

✔ Use meaningful function names.

✔ Keep functions small.

✔ One function should perform one task.

✔ Avoid unnecessary global variables.

✔ Use return whenever needed.

✔ Write reusable functions.

---

# 📌 Common Errors

❌ Forgetting to call the function.

❌ Wrong number of arguments.

❌ Missing return statement.

❌ Wrong indentation.

❌ Using local variables outside the function.

---

# 📌 Summary

Today I learned

✅ What is Function

✅ Advantages of Functions

✅ Built-in Functions

✅ User-defined Functions

✅ Parameters

✅ Arguments

✅ Types of Arguments

✅ Return Statement

✅ Local Variables

✅ Global Variables

✅ Scope

✅ Lambda Function

✅ Recursion (Introduction)

Functions are one of the most important concepts in Python because they make code reusable, modular, clean, and easy to maintain. Every professional Python developer uses functions extensively in real-world applications.