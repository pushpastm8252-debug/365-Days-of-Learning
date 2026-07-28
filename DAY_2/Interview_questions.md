# Python Day 2 Interview Questions

## 1. What is an Operator in Python?

Answer:

Operator is a symbol that performs operations on variables and values.

Example:

a = 10
b = 5

print(a+b)


---

## 2. What are the types of operators in Python?

Answer:

Python has six main operators:

1. Arithmetic Operator
2. Assignment Operator
3. Comparison Operator
4. Logical Operator
5. Membership Operator
6. Identity Operator


---

## 3. Difference between / and // operator?

Answer:

/ gives normal division result.

Example:

10/3

Output:
3.33


// gives floor division result.

Example:

10//3

Output:
3


---

## 4. What is modulus operator (%)?

Answer:

Modulus operator returns remainder.

Example:

10 % 3

Output:

1


---

## 5. What is a string in Python?

Answer:

String is a collection of characters enclosed inside quotes.

Example:

name="Python"


---

## 6. What is indexing in string?

Answer:

Indexing is accessing individual characters from string.

Example:

text="Python"

text[0]

Output:

P


---

## 7. What is string slicing?

Answer:

Slicing is extracting a part of string.

Example:

text[0:3]

Output:

Pyt


---

## 8. What is type casting?

Answer:

Type casting is converting one datatype into another datatype.


Example:

x="100"

y=int(x)


---

## 9. Why do we use int() function?

Answer:

int() converts value into integer datatype.


---

## 10. Why input() needs type casting?

Answer:

Because input() always returns data as string.

Example:

age=input()

returns:

"20"


To convert:

age=int(input())


---

## 11. Difference between == and is?

Answer:

== checks values.

is checks memory location.


---

## 12. What is bool()?

Answer:

bool() converts value into True or False.


Example:

bool(5)

Output:

True