'''Single Inheritance'''

#Q1. Create a class Person with attributes name and age, and a method display() to print them. Create a class Employee that inherits from Person and adds an attribute salary with a method to display all details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)   #Super() is used to call parent class constructor.
        self.salary = salary
    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

e1 = Employee("Mansi Sakhare", 22, 80000)
e1.display()


#Q2. Create a class Vehicle with a method fuel_type() that prints "Uses petrol/diesel". Create a class Car that inherits from Vehicle, adds a method num_wheels() that prints "4 wheels", and calls both methods from an object of Car.
class Vehicle:
    def fuel_type(self):
        print("Uses Petrol")
        
class Car(Vehicle):
    def num_wheels(self):
        print("4 wheels")

c1=Car()
c1.fuel_type()
c1.num_wheels()


'''Hierarchical Inheritance'''

#Q3. Create a base class Shape with a method info() that prints "This is a shape". Create two classes Circle and Rectangle that both inherit from Shape. Add a method area() in each to calculate and print their respective areas (take radius/length & breadth as input).
class Shape(self):
    def info(self):
        print("This is a shape")

class Circle(Shape):
    def area(self):
        radius=float(input("Enter radius:"))