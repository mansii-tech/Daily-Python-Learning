'''Q1. Class and Object 
Create a class Student with attributes name and marks. Add a method display() that prints both. Create two objects and call display() on each.
'''
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name",self.name)
        print("Marks",self.marks)
s1 = Student("Mansi",85)
s2 = Student("Rahul",90)
s1.display()
s2.display()
              

'''Q2. Methods with Calculation 
Create a class Rectangle with attributes length and width. Add methods area() and perimeter(). Create an object with length 8 and width 5, and print both results.
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area:",self.length * self.width)
    def perimeter(self):
        print("Perimeter:", 2* (self.length + self.width))

r = Rectangle(4,8)
r.area()
r.perimeter()


'''Q3. Constructor with Default Value 
Create a class Counter whose constructor sets count = 0. Add methods increment(), decrement() and show(). Call increment() three times, decrement() once, then show the final count.
'''
class Counter:
    def __init__(self):
       self.count=0
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def show(self):
        print("Count:", self.count)
c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
c.show()
  

'''Q4. Inheritance 
Create a parent class Person with attributes name and age and a method display(). Create a child class Student that inherits from Person, adds a roll_no attribute, and uses super() in its constructor. Override display() in Student so it prints all three details. Create a Student object and call display().
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    def display(self):
        print(self.name, self.age, self.roll_no)
s = Student("Mansi",0, 10)
s.display()