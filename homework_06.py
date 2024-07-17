#problem 0
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# Instantiate an object of the Person class
person = Person("Julia", 23)

# Print the object, which will use the __str__ method
print(person)

#problem 1
class Email:
    def __init__(self, address):
        self.address = address

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.address.lower() == other.address.lower()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)



email1 = Email("user@example.com")
email2 = Email("user@example.com")
email3 = Email("User@Example.com")
email4 = Email("different@example.com")


print(email1 == email2)
print(email1 == email3)
print(email1 == email4)

# Test inequality
print(email1 != email2)
print(email1 != email3)
print(email1 != email4)

#problem 2
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age


    def get_name(self):
        return self._name


    def set_name(self, name):
        self._name = name


    def get_age(self):
        return self._age


    def set_age(self, age):
        self._age = age

# Demonstrate usage
student1 = Student("Alice", 20)
print(student1.get_name())
print(student1.get_age())

student1.set_name("Bob")
student1.set_age(25)
print(student1.get_name())
print(student1.get_age())


#Problem 3

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def balance_inquiry(self):
        return self._balance

# Demonstrate usage
account1 = BankAccount(100)
print(account1.balance_inquiry())

account1.deposit(50)
print(account1.balance_inquiry())

account1.withdraw(30)
print(account1.balance_inquiry())


#Problem 4

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


    def __eq__(self, other):
        return self.area() == other.area()


    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

# Test the comparison operators
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)

print(rectangle1 == rectangle2)
print(rectangle1 < rectangle2)

#Problem 5
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bicycle(Vehicle):
    def start_engine(self):
        print("Bicycle does not have an engine")


car1 = Car()
bicycle1 = Bicycle()

car1.start_engine()
bicycle1.start_engine()

#Problem 6

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

# Demonstrate usage
book1 = Book("The Great Gatsby", "F. S. Fitzgerald", 180)
print(book1)
print(len(book1))

#Problem 7

class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __str__(self):
        return f"I am a {self.species}, specifically a dog."

class Cat(Animal):
    def __str__(self):
        return f"I am a {self.species}, specifically a cat."


dog1 = Dog("Canine")
cat1 = Cat("Feline")

print(dog1)
print(cat1)

#Problem 8

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary


    def get_name(self):
        return self._name


    def get_salary(self):
        return self._salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department


    def get_department(self):
        return self._department


manager1 = Manager("Bobby", 50000, "Sales")

print(manager1.get_name())
print(manager1.get_salary())
print(manager1.get_department())

#Problem 9

import datetime

class Employee:
    def __init__(self, name, start_date, pin, phone, address, manager_name, department):
        self.name = name
        self.start_date = start_date
        self.pin = pin
        self.phone = phone
        self.address = address
        self.manager_name = manager_name
        self.department = department

    def calculate_tenure(self):
        start_date = datetime.datetime.strptime(self.start_date, "%Y-%m-%d")
        today = datetime.datetime.now()
        tenure = today - start_date
        return tenure.days // 365

    def business_card_info(self):
        return f"Name: {self.name}\nDepartment: {self.department}\nPhone: {self.phone}"

# Demonstrate usage
employee1 = Employee("Alice", "2020-01-01", "1234", "123-456-7890", "123 Main St", "Jane Smith", "Sales")

print(employee1.calculate_tenure())
print(employee1.business_card_info())




