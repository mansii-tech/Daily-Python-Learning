'''Multi-level Inheritance'''

class Person:
    def get_name(self,name):
      self.name=name
      return self.name
class Employee(Person):
    def get_salary(self,salary):
        self.salary=salary
        return self.salary
class Parttime_Employee(Employee):
    def get_hours(self,hours):
        self.no_hours=hours
        return self.no_hours
    
p=Parttime_Employee()
print(f"name {p.get_name('monali')}")
print(f"salary {p.get_salary(20000)}")
print(f"no of hours {p.get_hours(5)}")