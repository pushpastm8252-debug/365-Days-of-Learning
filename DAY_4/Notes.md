# 📚 Day 4 - Python Loops

## 🎯 Objective

Today I learned one of the most important concepts in Python—**Loops**.

Loops help us execute the same block of code multiple times without writing it repeatedly.

---

# 🔹 What is a Loop?

A loop is a programming statement that repeats a block of code until a condition becomes False or a sequence ends.

Instead of writing the same code again and again, we use loops.

### Example

Without Loop

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

With Loop

for i in range(5):
    print("Hello")

The output is the same, but the code is much shorter and easier to understand.

---

# 🔹 Why Do We Use Loops?

Loops are used because they:

✅ Reduce code repetition

✅ Save time

✅ Make programs shorter

✅ Improve readability

✅ Help solve large problems easily

---

# 🔹 Types of Loops in Python

Python has two main types of loops.

1. for Loop

2. while Loop

---

# 🔹 for Loop

A for loop is used when we know how many times we want to repeat a task.

### Syntax

for variable in sequence:
    statement

Example

for i in range(5):
    print(i)

Output

0
1
2
3
4

---

# 🔹 while Loop

A while loop repeats until a condition becomes False.

### Syntax

while condition:
    statement

Example

i = 1

while i <= 5:
    print(i)
    i += 1

Output

1
2
3
4
5

---

# 🔹 Difference Between for and while Loop

| for Loop | while Loop |
|-----------|------------|
| Used when number of iterations is known | Used when condition controls repetition |
| Easier to write | Requires manual update |
| Uses range() or collections | Uses Boolean condition |

---

# 🔹 range() Function

The range() function generates a sequence of numbers.

### Syntax

range(stop)

range(start, stop)

range(start, stop, step)

### Examples

range(5)

Output

0 1 2 3 4

---

range(1,6)

Output

1 2 3 4 5

---

range(2,11,2)

Output

2 4 6 8 10

---

# 🔹 break Statement

The break statement immediately stops the loop.

Example

for i in range(10):
    if i == 5:
        break
    print(i)

Output

0
1
2
3
4

---

# 🔹 continue Statement

continue skips the current iteration and moves to the next iteration.

Example

for i in range(6):
    if i == 3:
        continue
    print(i)

Output

0
1
2
4
5

---

# 🔹 pass Statement

pass is a placeholder statement.

It does nothing but prevents syntax errors.

Example

for i in range(5):
    pass

---

# 🔹 Nested Loop

A loop inside another loop is called a Nested Loop.

Example

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

Nested loops are mostly used for Pattern Printing.

---

# 🔹 Pattern Printing

Pattern printing is one of the best ways to improve loop logic.

Common patterns are:

⭐ Right Triangle

⭐ Inverted Triangle

⭐ Pyramid

⭐ Diamond

⭐ Hollow Square

⭐ Number Pattern

⭐ Alphabet Pattern

---

# 🔹 Real-Life Applications of Loops

Loops are used in many real-world applications.

✔ ATM Machine

✔ Login System

✔ Mobile Apps

✔ Banking Software

✔ Data Processing

✔ AI & Machine Learning

✔ Games

✔ Automation Scripts

✔ Web Development

---

# 🔹 Advantages of Loops

✅ Reduce code length

✅ Save development time

✅ Easy to maintain

✅ Improve efficiency

✅ Better logic building

---

# 🔹 Common Mistakes

❌ Infinite Loop

Example

while True:
    print("Hello")

This loop never stops.

---

❌ Forgetting to update the variable

Example

i = 1

while i <= 5:
    print(i)

This creates an infinite loop because i never changes.

---

❌ Wrong indentation

Python uses indentation to define blocks of code.

Incorrect indentation causes errors.

---

# 🔹 Best Practices

✔ Choose the correct loop.

✔ Use meaningful variable names.

✔ Avoid unnecessary nested loops.

✔ Keep conditions simple.

✔ Use break only when required.

✔ Use continue carefully.

---

# 🔹 Summary

Today I learned:

✅ What is Loop

✅ Why Loops are used

✅ Types of Loops

✅ for Loop

✅ while Loop

✅ range() Function

✅ break Statement

✅ continue Statement

✅ pass Statement

✅ Nested Loop

✅ Pattern Printing

Loops are one of the most important concepts in programming. They help automate repetitive tasks, improve code efficiency, and strengthen logical thinking. Mastering loops is essential for solving coding problems, DSA, and real-world programming challenges.

---