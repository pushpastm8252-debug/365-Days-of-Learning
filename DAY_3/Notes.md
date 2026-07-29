# 📚 Day 3 Notes
# Python Conditional Statements

---

# What is Decision Making?

Decision making means allowing a program to choose what to do based on a condition.

Example:

If it is raining,
carry an umbrella.

Otherwise,
don't carry an umbrella.

Python follows the same logic.

---

# What is if Statement?

The if statement executes a block of code only when the condition is True.

Syntax

if condition:
    statement

Example

age = 18

if age >= 18:
    print("Eligible to Vote")

---

# How if Works

Condition → True

↓

Execute Code

Condition → False

↓

Skip Code

---

# if Statement Flow

Start

↓

Condition

↓

True?

↓

Yes

↓

Execute

↓

End

No

↓

End

---

# if-else Statement

Sometimes we want another block of code to execute if the condition becomes False.

Syntax

if condition:
    statement
else:
    statement

Example

marks = 45

if marks >= 33:
    print("Pass")
else:
    print("Fail")

---

# Flow of if-else

Start

↓

Condition

↓

True?

↓

Yes → Execute if block

↓

End

No

↓

Execute else block

↓

End

---

# elif Statement

elif means Else If.

Used when multiple conditions are present.

Syntax

if condition:
    statement

elif condition:
    statement

else:
    statement

Example

marks = 82

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("Fail")

---

# Nested if

Nested if means an if statement inside another if statement.

Example

if age >=18:

    if citizen == "yes":

        print("Eligible")

---

# Why Nested if?

Used when more than one condition must be checked.

Example

ATM

Card inserted?

↓

PIN Correct?

↓

Withdraw Money

---

# Comparison Operators

Comparison operators compare two values.

Operator Meaning

== Equal

!= Not Equal

> Greater Than

< Less Than

>= Greater Than or Equal

<= Less Than or Equal

Example

10 > 5

Result

True

---

# Logical Operators

Logical operators combine multiple conditions.

AND

Both conditions must be True.

Example

age >=18 and citizen=="yes"

OR

Any one condition should be True.

Example

marks>=33 or sports=="yes"

NOT

Reverses the result.

Example

not(age<18)

---

# Truth Table

AND

True True → True

True False → False

False True → False

False False → False

---

OR

True True → True

True False → True

False True → True

False False → False

---

NOT

True → False

False → True

---

# Indentation

Python uses indentation instead of braces.

Correct

if age>=18:
    print("Adult")

Wrong

if age>=18:
print("Adult")

IndentationError

---

# Difference

if

Checks one condition.

if-else

Checks one condition with two possible outputs.

elif

Checks multiple conditions.

Nested if

Checks conditions inside conditions.

---

# Real-Life Examples

Voting System

ATM Machine

Student Grade

Weather Report

Traffic Signal

Login System

Bank Verification

Electricity Bill

BMI Category

Leap Year

---

# Advantages

Easy to understand

Improves decision making

Makes programs intelligent

Used in almost every application

---

# Disadvantages

Too many nested conditions reduce readability.

---

# Best Practices

Use meaningful variable names.

Keep conditions simple.

Avoid unnecessary nesting.

Use elif instead of multiple if when possible.

Maintain proper indentation.

---

# Summary

Today I learned:

✔ if Statement

✔ if-else

✔ elif

✔ Nested if

✔ Comparison Operators

✔ Logical Operators

✔ Decision Making

✔ Indentation

These concepts are the foundation of Python programming and are essential for building real-world applications.