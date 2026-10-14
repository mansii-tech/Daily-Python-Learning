class Student:
    def __init__(self, name,roll no,address[0]):   #Constructor
        self.name = name
        self.rollno = rollno
        self.address = []
    def add.address(self,address):
        self.address.append(address)

class Address:
    def __init__(self,locality,state,city):
        self.locality=locality
        self.state=state
        self.city=city
        
        
s=Student('Mansi',14)   #it will call customer class constructor
a=Address('Sidhrath tailor shop','Maharashtra','Nagpur')    #it will call account class constructor
c.add_address(a)
print("Student details")
print(f"student id : {s.student_id}")
print(f"address : {a.address}")