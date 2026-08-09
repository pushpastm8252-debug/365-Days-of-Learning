# 🐍 Day 10 - Object-Oriented Programming (OOP)

# 1. What is OOP?

OOP stands for **Object-Oriented Programming**.

It is a programming approach where programs are designed using **classes and objects**.

OOP helps us organize large programs, reuse code, and represent real-world entities.

Examples of real-world objects:

- Student
- Car
- Bank Account
- Employee
- Mobile Phone

---

# 2. What is a Class?

A class is a blueprint or template for creating objects.

Example:

```python
class Student:
    pass
```

Here, `Student` is a class.

---

# 3. What is an Object?

An object is an instance of a class.

Example:

```python
class Student:
    pass

s1 = Student()
s2 = Student()
```

Here:

```text
Student → Class
s1      → Object
s2      → Object
```

---

# 4. Creating a Class and Object

```python
class Student:

    def display(self):
        print("I am a student")


s1 = Student()

s1.display()
```

Output:

```text
I am a student
```

---

# 5. self Keyword

`self` refers to the current object.

Example:

```python
class Student:

    def display(self):
        print("Hello")


s1 = Student()
s1.display()
```

The `self` parameter allows the method to access the current object's data.

---

# 6. Constructor

A constructor is a special method that is automatically called when an object is created.

In Python, the constructor is:

```python
__init__()
```

Example:

```python
class Student:

    def __init__(self):
        print("Object Created")


s1 = Student()
```

Output:

```text
Object Created
```

---

# 7. Constructor with Parameters

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Pushpa", 20)

s1.display()
```

---

# 8. Instance Variables

Instance variables belong to a particular object.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Pushpa", 20)
s2 = Student("Rahul", 21)

print(s1.name)
print(s2.name)
```

Each object has its own data.

---

# 9. Instance Methods

Methods that operate on object data are called instance methods.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


s1 = Student("Pushpa")

s1.display()
```

---

# 10. Class Variables

A class variable is shared by all objects of the class.

Example:

```python
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


s1 = Student("Pushpa")
s2 = Student("Rahul")

print(s1.college)
print(s2.college)
```

---

# 11. Class Method

A class method works with class-level data.

It uses the `@classmethod` decorator.

Example:

```python
class Student:

    college = "ABC College"

    @classmethod
    def display_college(cls):
        print(cls.college)


Student.display_college()
```

---

# 12. Static Method

A static method does not depend on object or class data.

It uses the `@staticmethod` decorator.

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

Output:

```text
30
```

---

# 13. Encapsulation

Encapsulation means wrapping data and methods together inside a class and controlling access to data.

Example:

```python
class Bank:

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(self.balance)


b = Bank(5000)

b.show_balance()
```

---

# 14. Public Members

Public members can be accessed directly.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Pushpa"


s = Student()

print(s.name)
```

---

# 15. Protected Members

Protected members are conventionally represented using a single underscore `_`.

Example:

```python
class Student:

    def __init__(self):
        self._marks = 90


s = Student()

print(s._marks)
```

The underscore indicates that the member is intended for internal or subclass use.

---

# 16. Private Members

Private members are represented using double underscore `__`.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)


s = Student()

s.show_marks()
```

---

# 17. Inheritance

Inheritance allows one class to acquire properties and methods from another class.

Example:

```python
class Animal:

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()
```

---

# 18. Single Inheritance

One child class inherits from one parent class.

```python
class Parent:

    def show(self):
        print("Parent")


class Child(Parent):

    def display(self):
        print("Child")


c = Child()

c.show()
c.display()
```

---

# 19. Multiple Inheritance

One child class inherits from multiple parent classes.

```python
class Father:

    def skill1(self):
        print("Driving")


class Mother:

    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()

c.skill1()
c.skill2()
```

---

# 20. Multilevel Inheritance

Inheritance occurs across multiple levels.

```python
class Grandparent:

    def show1(self):
        print("Grandparent")


class Parent(Grandparent):

    def show2(self):
        print("Parent")


class Child(Parent):

    def show3(self):
        print("Child")


c = Child()

c.show1()
c.show2()
c.show3()
```

---

# 21. Hierarchical Inheritance

Multiple child classes inherit from one parent class.

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.eat()
c.eat()
```

---

# 22. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance.

Example:

```text
        A
       / \
      B   C
       \ /
        D
```

Python supports such inheritance through multiple inheritance.

---

# 23. super()

`super()` is used to access methods or the constructor of the parent class.

Example:

```python
class Parent:

    def __init__(self):
        print("Parent Constructor")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")


c = Child()
```

Output:

```text
Parent Constructor
Child Constructor
```

---

# 24. Polymorphism

Polymorphism means **one interface with different behaviors**.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()
```

Output:

```text
Bark
Meow
```

---

# 25. Method Overriding

When a child class provides its own version of a parent method, it is called method overriding.

Example:

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()
```

Output:

```text
Bark
```

---

# 26. Method Overloading

Traditional method overloading is not supported in Python in the same way as languages such as Java.

Python commonly achieves similar behavior using:

- Default arguments
- `*args`
- `**kwargs`

Example:

```python
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


c = Calculator()

print(c.add(10))
print(c.add(10, 20))
print(c.add(10, 20, 30))
```

---

# 27. Abstraction

Abstraction means hiding implementation details and showing only the required functionality.

Python provides abstract classes through the `abc` module.

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()
```

---

# 28. Abstract Class

A class containing one or more abstract methods is called an abstract class.

Example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

A child class must implement the abstract method before its object can normally be created.

---

# 29. Getter and Setter

Getters are used to retrieve data.

Setters are used to modify data.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


s = Student()

s.set_marks(90)

print(s.get_marks())
```

---

# 30. Composition

Composition means one class contains an object of another class.

Example:

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()


c = Car()

c.start_car()
```

---

# 31. Aggregation

Aggregation represents a relationship where one object uses another object, but the contained object can exist independently.

Example:

```python
class Teacher:

    def teach(self):
        print("Teaching")


class School:

    def __init__(self, teacher):
        self.teacher = teacher

    def start_class(self):
        self.teacher.teach()


t = Teacher()

s = School(t)

s.start_class()
```

---

# 🧠 Four Main Pillars of OOP

## 1. Encapsulation

Wrapping data and methods together.

## 2. Inheritance

Reusing properties and methods from another class.

## 3. Polymorphism

Same interface with different behavior.

## 4. Abstraction

Hiding unnecessary implementation details.

---

# 🔥 Important OOP Keywords

```text
class
object
self
__init__
super
@classmethod
@staticmethod
@abstractmethod
ABC
```

---

# 📌 Class vs Object

| Class | Object |
|---|---|
| Blueprint | Instance |
| Logical entity | Real instance |
| Does not represent a specific object | Represents a specific instance |
| Example: Student | Example: s1 |

---

# 📌 Instance Variable vs Class Variable

| Instance Variable | Class Variable |
|---|---|
| Belongs to object | Belongs to class |
| Usually accessed using self | Can be accessed through class/object |
| Different for each object | Shared by objects |

---

# 📌 Instance Method vs Class Method vs Static Method

| Type | First Parameter | Used For |
|---|---|---|
| Instance Method | self | Object data |
| Class Method | cls | Class data |
| Static Method | None required | Independent utility logic |

---

# 📌 Summary

✅ OOP

✅ Class

✅ Object

✅ Constructor

✅ `__init__()`

✅ `self`

✅ Instance Variables

✅ Instance Methods

✅ Class Variables

✅ Class Methods

✅ Static Methods

✅ Encapsulation

✅ Public Members

✅ Protected Members

✅ Private Members

✅ Inheritance

✅ Single Inheritance

✅ Multiple Inheritance

✅ Multilevel Inheritance

✅ Hierarchical Inheritance

✅ Hybrid Inheritance

✅ Polymorphism

✅ Method Overriding

✅ Method Overloading Concepts

✅ Abstraction

✅ Abstract Classes

✅ `super()`

✅ Getters & Setters

✅ Composition

✅ Aggregation