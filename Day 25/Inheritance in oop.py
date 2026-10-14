#create a class saving
class Saving:
    def __init__ (self,actno,bal):   #creating constructor from line 3 to 10
        self.actno=actno
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("Amount deposited successfully")
    def show_balance(self):
        return f"balance is {self.bal}"
a=int(input("enter account number"))    #creating method from line 11 to 16
b=int(input("enter account balance"))
s=Saving(a,b)
amt=int(input("enter account to be deposited"))
s.deposit(amt)       #creating object
print(s.show_balance())


#Single Inheritance
class Person:
    def get_persondata(self,name,address):
        self.name=name
        self.address=address
class Student(Person):#student is a child class of person class
  def get_studentdata(self,rno,marks):
        self.rno=rno
        self.marks=marks
        
        
#creating object of student class
s1=Student()
s1.get_persondata("subhan","yawatmal")
s1.get_studentdata(123,999)
print("student details")
print(f"rno :{s1.rno},marks:{s1.marks},name:{s1.name},address:{s1.address}")

















