#Example of simple methodv Overriding (Overriding Inheritance main hota hai)
#1.
class Account:
    def deposite(self):
        print("Deposit method of account class")
class Saving(Account):
    #Overriding the base class deposit method
    def deposit(self):
        print("Deposite method of saving class")
        
s=Saving()
s.deposit()


#2.
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}") 

s=Saving()
s.deposit(200)

#3.
class Account:
    bal=1000
    def deposit(self,amount):
        print("deposit method of account class")
class Saving(Account):
    #overriding the base class deposit method
    def deposit(self,amount):
        self.interest=500
        self.bal=self.bal+amount+self.interest
        print(f"amount deposited , bal is {self.bal}") 
class Current(Account):
    #Overriding the base class deposit method
    def deposit(self,amount):
        self.bal=self.bal+amount
        print(f"Amount deposited without interest,bal is {self.bal}")
s=Saving()
s.deposit(200)
c=Current()
c.deposit(200)


#Example of Overriding (method and with constructor)
#child class se parent class ko bula rhe hein using super()
class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name:{self.name}"
class Student(Person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno:{self.rno}"
s=Student("Mansi",12)
print(s.display())


#example of method overriding
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return f"name : {self.name}"
class student(person):
    def __init__(self,name,rno):
        super().__init__(name)
        self.rno=rno
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
class parttime_student(student):
    def __init__(self,name,rno,course):
        super().__init__(name,rno)
        self.course=course
    def display(self):
        print(super().display())
        return f"course : {self.course}"

#creating objectpt=parttime_student("amit",123,"python")
print(pt.display())

