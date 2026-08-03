# 📘 Day 7 Notes – Python Dictionaries, Tuples & Sets

# 🐍 1. Dictionary (dict)

A Dictionary is a built-in Python data structure that stores data in **key-value pairs**. Each key is unique and is used to access its corresponding value.

## Syntax

```python
student = {
    "name": "Pushpa",
    "age": 20,
    "course": "B.Tech CSE"
}
```

## Output

```python
{
'name':'Pushpa',
'age':20,
'course':'B.Tech CSE'
}
```

---

## Characteristics of Dictionary

- Stores data in key-value pairs.
- Mutable (values can be changed after creation).
- Ordered (Python 3.7+ preserves insertion order).
- Keys must be unique.
- Keys must be immutable (string, integer, tuple, etc.).
- Values can be duplicated.
- Supports nested dictionaries.

---

## Accessing Elements

```python
print(student["name"])
```

Output

```text
Pushpa
```

Using `get()`

```python
print(student.get("age"))
```

Output

```text
20
```

Using a default value

```python
print(student.get("city", "Not Found"))
```

Output

```text
Not Found
```

---

## Updating Dictionary

```python
student["age"] = 21
```

Output

```python
{'name':'Pushpa','age':21,'course':'B.Tech CSE'}
```

---

## Adding New Item

```python
student["city"] = "Patna"
```

Output

```python
{
'name':'Pushpa',
'age':21,
'course':'B.Tech CSE',
'city':'Patna'
}
```

---

## Deleting Items

```python
del student["course"]
```

```python
student.pop("city")
```

```python
student.clear()
```

---

## Important Dictionary Methods

| Method | Description |
|---------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Returns value safely |
| update() | Updates dictionary |
| pop() | Removes specific key |
| popitem() | Removes last inserted item |
| clear() | Removes all items |
| copy() | Creates a copy |
| len() | Returns total number of items |

---

# 📦 2. Tuple (tuple)

A Tuple is an ordered collection used to store multiple values. Unlike a list, tuples cannot be modified after creation.

## Syntax

```python
numbers = (10, 20, 30, 40, 50)
```

---

## Characteristics

- Ordered
- Immutable
- Allows duplicate values
- Faster than list
- Supports indexing and slicing
- Can store different data types

Example

```python
data = ("Python", 10, 3.5, True)
```

---

## Access Elements

```python
print(numbers[0])
```

Output

```text
10
```

Last Element

```python
print(numbers[-1])
```

Output

```text
50
```

---

## Slicing

```python
print(numbers[1:4])
```

Output

```text
(20, 30, 40)
```

---

## Tuple Methods

### count()

```python
t = (1,2,2,3)
print(t.count(2))
```

Output

```text
2
```

### index()

```python
print(t.index(3))
```

Output

```text
3
```

---

## Useful Functions

```python
len(numbers)
sum(numbers)
max(numbers)
min(numbers)
```

---

## Advantages

- Faster than lists.
- Prevents accidental modification.
- Useful for fixed data like coordinates, months, and days.

---

# 🎯 3. Set (set)

A Set is an unordered collection of unique elements. Duplicate values are automatically removed.

## Syntax

```python
numbers = {1,2,3,4}
```

---

## Characteristics

- Unordered
- Mutable
- No duplicate values
- No indexing
- Very fast searching
- Supports mathematical operations

Example

```python
numbers = {1,2,2,3,3,4}
```

Output

```text
{1,2,3,4}
```

---

## Adding Elements

```python
numbers.add(5)
```

---

## Removing Elements

```python
numbers.remove(2)
```

Safe Removal

```python
numbers.discard(10)
```

---

## Set Operations

### Union

```python
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
```

Output

```text
{1,2,3,4,5}
```

---

### Intersection

```python
print(A.intersection(B))
```

Output

```text
{3}
```

---

### Difference

```python
print(A.difference(B))
```

Output

```text
{1,2}
```

---

### Symmetric Difference

```python
print(A.symmetric_difference(B))
```

Output

```text
{1,2,4,5}
```

---

## Useful Set Methods

| Method | Description |
|---------|-------------|
| add() | Add element |
| remove() | Remove element |
| discard() | Remove safely |
| pop() | Remove random element |
| clear() | Remove all elements |
| union() | Combine sets |
| intersection() | Common elements |
| difference() | Difference |
| symmetric_difference() | Non-common elements |
| copy() | Copy set |
| len() | Returns total elements |

---

# 📊 List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|------|------------|
| Ordered | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Duplicate Values | ✅ Yes | ✅ Yes | ❌ No | Values Yes, Keys No |
| Indexing | ✅ Yes | ✅ Yes | ❌ No | By Key |
| Syntax | [] | () | {} | {key:value} |

---

# 📝 When to Use

### List

- Data changes frequently.
- Need indexing.
- Need duplicate values.

```python
students = ["A","B","C"]
```

---

### Tuple

- Fixed data.
- Better performance.
- Read-only records.

```python
months = ("Jan","Feb","Mar")
```

---

### Set

- Remove duplicates.
- Perform union/intersection.
- Fast membership testing.

```python
unique_numbers = {1,2,3,4}
```

---

### Dictionary

- Store key-value data.
- Fast searching.
- Real-world records.

```python
student = {
    "name":"Pushpa",
    "age":20
}
```

---

# 💡 Real-Life Examples

- Dictionary → Student Record, Contact Book, Employee Details
- Tuple → GPS Coordinates, RGB Colors, Days of Week
- Set → Unique Visitors, Tags, Email IDs
- List → Shopping Cart, To-Do List, Student Marks

---

# 🎯 Summary

- Dictionary stores data in key-value pairs.
- Tuple stores ordered and immutable data.
- Set stores unique unordered elements.
- List stores ordered and mutable collections.
- Choose the data structure according to your problem.