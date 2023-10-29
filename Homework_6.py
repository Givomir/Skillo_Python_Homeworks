
###################################################################################################
###################################################################################################
#problem 0
#Create a class "Person" with a special method "__str__" to provide a string representation.
# Instantiate an object of this class and print it.:
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


person = Person("Georgi Iliev Dimitrov", 30, "zhk Geo Milev, ulitsa Kostenski vodopad 25A")

print("Answer for problem 0:")
print(person)


###################################################################################################
###################################################################################################
#problem 1
#Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses.
# Test the equality and inequality operators with different email instances.:

class Email:
    def __init__(self, address):
        self.address = address

    def __eq__(self, other):

        if isinstance(other, Email):
            return self.address == other.address
        return False

    def __ne__(self, other):

        return not self.__eq__(other)

email1 = Email("Georgi_Ivanov@example.com")
email2 = Email("Georgi.Ivanov@example.com")
email3 = Email("Georgi_Ivanov@example.com")

print("\n Answer for problem 1:")

print(email1 == email2)
print(email1 == email3)

print(email1 != email2)
print(email1 != email3)


###################################################################################################
###################################################################################################
#problem 2
#Create a class "Student" with private attributes for name and age.
#Implement getter and setter methods for these attributes.
#Demonstrate their usage.:

class Student:
    def __init__(self, name, age):
        self._name = name  # _name is a convention for a "protected" attribute
        self._age = age


    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age


student = Student("Georgi", 19)
print("\n Answer for problem 2:")

print("Initial values:")
print("Name:", student.get_name())
print("Age:", student.get_age())

student.set_name("Petar")
student.set_age(21)

print("\nModified values:")
print("Name:", student.get_name())
print("Age:", student.get_age())


###################################################################################################
###################################################################################################
#problem 3
#Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry.
#Use encapsulation to protect the account balance.
#Demonstrate proper usage of the class.:

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def balance_inquiry(self):
        return f"Account balance for {self._account_holder}'s account ({self._account_number}): ${self._balance:.2f}"

# Demonstrate proper usage of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.0)
print("\n Answer for problem 3:")
print(account.balance_inquiry())
print(account.deposit(500.50))
print(account.withdraw(200.75))
print(account.withdraw(1500.0))


###################################################################################################
###################################################################################################
#problem 4
#Implement a class "Rectangle" with private attributes for length and width.
#Include special methods "__eq__" and "__lt__" to compare rectangles based on area and perimeter.
#Test the comparison operators with multiple instances.:

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area() and self.perimeter() == other.perimeter()
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area() and self.perimeter() < other.perimeter()
        return False

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)
rectangle3 = Rectangle(4, 5)

print("\n Answer for problem 4:")
print("Are rectangle1 and rectangle2 equal (based on area and perimeter)?", rectangle1 == rectangle2)
print("Is rectangle1 less than rectangle2 (based on area and perimeter)?", rectangle1 < rectangle2)
print("Are rectangle1 and rectangle3 equal?", rectangle1 == rectangle3)


###################################################################################################
###################################################################################################
#problem 5
#Design an abstract class "Vehicle" with a method "start_engine()".
#Create two subclasses, "Car" and "Bicycle," implementing the "start_engine()" method differently.
#Demonstrate polymorphism by calling the method on instances of both subclasses.:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Bicycle(Vehicle):
    def start_engine(self):
        return "Bicycle doesn't have an engine."

car = Car()
bicycle = Bicycle()

print("\n Answer for problem 5:")
print(car.start_engine())
print(bicycle.start_engine())


###################################################################################################
###################################################################################################
#problem 6
#Implement a class "Book" with special methods "__str__" and "__len__"
#to provide a string representation and the number of pages.
#Create instances of "Book" and demonstrate the use of these methods.:

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

# Create instances of the Book class
book1 = Book("Отнесени от вихъра", "Франк Лойд Райд", 180)
book2 = Book("Опасен чар", "Тодор Колев", 281)

print("\n Answer for problem 6:")

print(book1)
print(book2)

print(len(book1))  # Output: 180
print(len(book2))  # Output: 281


###################################################################################################
###################################################################################################
#problem 7
#Create a class "Animal" with a special method "__init__" that sets a species attribute.
#Implement subclasses "Dog" and "Cat" with their own "__str__" methods.
#Use polymorphism to display species information.:

class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __str__(self):
        return f"This is a {self.species}."

class Cat(Animal):
    def __str__(self):
        return f"This is a {self.species}."

# Create instances of Dog and Cat
dog = Dog("Dog")
cat = Cat("Cat")

print("\n Answer for problem 7:")
print(dog)  # Output: "This is a Dog."
print(cat)  # Output: "This is a Cat."


###################################################################################################
###################################################################################################
#problem 8
#Design a class "Employee" with encapsulated attributes for name and salary.
# Implement a subclass "Manager" that inherits from "Employee"
# and includes an additional attribute for the department.
# Use getters and setters to access and modify these attributes.:

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for salary
    def get_salary(self):
        return self._salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("Invalid salary value.")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    # Getter for department
    def get_department(self):
        return self._department

    # Setter for department
    def set_department(self, department):
        self._department = department

# Create instances of Employee and Manager
employee = Employee("Ivan Ivanov", 50000)
manager = Manager("Filip Dimitrov", 80000, "HR")
print("\n Answer for problem 8:")
# Access and modify attributes using getters and setters
print("Employee name:", employee.get_name())
employee.set_name("Kiril Kostov")
print("Updated employee name:", employee.get_name())

print("Employee salary:", employee.get_salary())
employee.set_salary(55000)
print("Updated employee salary:", employee.get_salary())

print("Manager department:", manager.get_department())
manager.set_department("Finance")
print("Updated manager department:", manager.get_department())


###################################################################################################
###################################################################################################
#problem 9
#Create a class called "Employee" that has attributes name, start_date, PIN,
#phone, address, manager_name, department.
#Decide their access scecifiers.
#Implement methods to calculate employee tenure, and business card info representation.:

class Employee:
    def __init__(self, name, start_date, pin, phone, address, manager_name, department):
        self.name = name
        self.start_date = start_date
        self._pin = pin
        self._phone = phone
        self._address = address
        self._manager_name = manager_name
        self._department = department

    def calculate_tenure(self):

        current_year = 2023
        start_year = int(self.start_date.split("/")[-1])
        tenure = current_year - start_year
        return tenure

    def business_card_info(self):
        return f"Name: {self.name}\nDepartment: {self._department}\nPhone: {self._phone}\nAddress: {self._address} \nmanager_name: {self._manager_name}"

# Create an instance of the Employee class
employee = Employee("Kiril Gospodinov", "01/15/2018", "1234", "555-555-5555", "Hajdushka gora 25B", "Branko Dimitrov", "HR")

# Calculate tenure and print business card info
tenure = employee.calculate_tenure()
business_card = employee.business_card_info()
print("\n Answer for problem 9:")
print(f"Tenure: {tenure} years")
print(business_card)


###################################################################################################
###################################################################################################
#problem 10
#Create an abstract class "Employee" with attributes for name and salary.
# Implement a subclass "Manager" that inherits from "Employee" and includes an additional
# attribute for the department.
# Ensure that the "Employee" class enforces encapsulation.
# Every employee and manager should have a method to send a message to.
# The message must be stored. Create a class "Team" that has a manager and a list of members.
# Implement a method that sends a message to everyone in the team.:


class Employee:
    def __init__(self, name, salary):
        self._name = name  # Employee name (Encapsulated attribute)
        self._salary = salary  # Employee salary (Encapsulated attribute)
        self._messages = []

    def send_message(self, message):
        self._messages.append(message)

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

class Team:
    def __init__(self, manager, members):
        self.manager = manager
        self.members = members

    def send_team_message(self, message):
        self.manager.send_message(message)
        for member in self.members:
            member.send_message(message)

# Create instances of Manager and Employee
manager = Manager("Georgi Pavlov", 80000, "HR")
employee1 = Employee("Sava Ivanov", 50000)
employee2 = Employee("Maria Petrova", 55000)


team = Team(manager, [employee1, employee2])

# Send a team message
team.send_team_message("Meeting at 2:00 PM")

# Display messages for the manager and team members
print("\n Answer for problem 10:")
print("Manager's Messages:", manager._messages)
print("Employee1's Messages:", employee1._messages)
print("Employee2's Messages:", employee2._messages)

