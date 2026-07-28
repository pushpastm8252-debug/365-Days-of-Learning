PYTHON NOTES
TOPIC: OPERATORS, STRING AND TYPE CASTING


==================================================
1. OPERATORS IN PYTHON
==================================================

Definition:
Operator is a symbol or keyword that is used to perform operations on variables and values.

Example:

a = 10
b = 5

print(a + b)

Output:
15


Types of Operators in Python:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators


==================================================
1. ARITHMETIC OPERATORS
==================================================

Arithmetic operators are used to perform mathematical calculations.

Operators:

+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus (Remainder)
**  Power
//  Floor Division


Example:

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)


Output:

13
7
30
3.33
1
1000
3


Explanation:

+  → Adds two values
-  → Subtracts two values
*  → Multiplies values
/  → Gives division result
%  → Gives remainder
** → Calculates power
// → Gives floor value


==================================================
2. ASSIGNMENT OPERATORS
==================================================

Assignment operators are used to assign values to variables.


Operator        Example          Meaning

=               x = 10           Assign value

+=              x += 5           x = x + 5

-=              x -= 5           x = x - 5

*=              x *= 5           x = x * 5

/=              x /= 5           x = x / 5



Example:

x = 10

x += 5

print(x)


Output:

15


==================================================
3. COMPARISON OPERATORS
==================================================

Comparison operators are used to compare two values.

The output of comparison operators is always True or False.


Operators:

==    Equal to

!=    Not Equal to

>     Greater than

<     Less than

>=    Greater than or equal to

<=    Less than or equal to



Example:

a = 10
b = 20

print(a == b)
print(a < b)


Output:

False
True



==================================================
4. LOGICAL OPERATORS
==================================================

Logical operators are used to combine multiple conditions.


Operators:


and

- Returns True when both conditions are True.


or

- Returns True if any one condition is True.


not

- Reverse the result.



Example:

age = 20

print(age > 18 and age < 30)


Output:

True



==================================================
5. MEMBERSHIP OPERATORS
==================================================

Membership operators check whether a value exists in a sequence.


Operators:


in

- Checks value is present.


not in

- Checks value is not present.



Example:

name = "Python"

print("P" in name)


Output:

True



==================================================
6. IDENTITY OPERATORS
==================================================

Identity operators are used to check whether two variables refer to the same object.


Operators:


is

- Returns True if both objects are same.


is not

- Returns True if objects are different.



Example:

a = 10
b = 10

print(a is b)


Output:

True



==================================================
2. STRING IN PYTHON
==================================================

Definition:

A string is a collection of characters written inside single quotes (' '),
double quotes (" ") or triple quotes (""" """).


Examples:

name = "Amir"

city = 'Delhi'

message = """Hello Python"""


print(name)



==================================================
STRING INDEXING
==================================================

Indexing means accessing individual characters of a string.

Index always starts from 0.


Example:

name = "Python"


P   y   t   h   o   n

0   1   2   3   4   5



Example:

text = "Python"

print(text[0])
print(text[3])


Output:

P
h



==================================================
STRING SLICING
==================================================

Slicing is used to get a part of a string.


Syntax:

string[start:end]


Example:

text = "Python"

print(text[0:3])


Output:

Pyt


Note:

Start index is included.

End index is not included.



==================================================
STRING METHODS
==================================================


1. upper()

Converts string into uppercase.


Example:

name = "python"

print(name.upper())


Output:

PYTHON



----------------------------------------------


2. lower()

Converts string into lowercase.


Example:

name = "PYTHON"

print(name.lower())


Output:

python



----------------------------------------------


3. replace()

Used to replace a word or character.


Example:

text = "Hello World"

print(text.replace("World","Python"))


Output:

Hello Python



----------------------------------------------


4. len()

Used to find length of string.


Example:

name = "Python"

print(len(name))


Output:

6



==================================================
3. TYPE CASTING IN PYTHON
==================================================

Definition:

Type casting means converting one data type into another data type.


Example:

a = "10"

b = int(a)

print(b)


Output:

10



==================================================
TYPES OF TYPE CASTING
==================================================


1. INTEGER CASTING (int)

Converts value into integer.


Example:

x = "50"

y = int(x)

print(y)


Output:

50



----------------------------------------------


2. FLOAT CASTING (float)

Converts value into decimal number.


Example:

x = 10

print(float(x))


Output:

10.0



----------------------------------------------


3. STRING CASTING (str)

Converts value into string.


Example:

number = 100

text = str(number)

print(text)


Output:

100



----------------------------------------------


4. BOOLEAN CASTING (bool)

Converts value into True or False.


Example:

x = 5

print(bool(x))


Output:

True



==================================================
IMPORTANT EXAMPLE OF TYPE CASTING
==================================================


Input function always returns string.


Example without casting:


age = input("Enter your age: ")

print(age + 5)


Output:

TypeError



Because:

"20" + 5

is not possible.



Correct way:


age = int(input("Enter your age: "))

print(age + 5)


Input:

20


Output:

25



==================================================
IMPORTANT POINTS TO REMEMBER
==================================================


1. Operators are used to perform operations.

2. String is a sequence of characters.

3. String indexing starts from 0.

4. Slicing is used to extract part of string.

5. input() always returns string.

6. Type casting converts one data type into another.

7. int(), float(), str(), bool() are common casting functions.



==================================================
PRACTICE QUESTIONS
==================================================


Q1. Write a program to add two numbers using operators.


Q2. Find the length of a string.


Q3. Convert string "100" into integer.


Q4. Check whether a word exists in a string.


Q5. Take age from user and print age after 5 years.



END OF NOTES