# learning instance wih example and constructor

# class customer:
#     def __init__(self):
#         name=""
#         mobile=0
# c1=customer()
# c1.name="manish"
# c1.mobile=123

# print(c1.name)
# print(c1.mobile)


#example of instance attribute  manually 
# for class attribute we give value upper then call it later
# but in instance we give value in same line
# class customer:
#    shopecode=111   #class atribute
# c1=customer()            # this is class attribute
# c1.name="manish"          # this is instance 
# c1.mobile=123

# print(c1.name)
# print(c1.mobile)

# example of constructor with parameters

# class customer:

#    def __init__(self,name,mobile):
#       self.name=name
#       self.mobile=mobile

# name=input("enter name:")
# mobile=int(input("enter mobile"))
# c1=customer(name,mobile)
# print(f"name:{c1.name}")
# print(f"mobile:{c1.mobile}")


# now we are making methods
class customer:

    def __init__(self,name,mobile):
      self.name=name
      self.mobile=mobile

#method
    def display(self):
        print(f"name:{name}")
        print(f"mobile:{mobile}")

name=input("enter name:")
mobile=int(input("enter mobile"))
c1=customer(name,mobile)
c1.display()
print(f"name:{c1.name}")
print(f"mobile:{c1.mobile}")


# example of create phone details

class Phone:
    # Class attribute (shared by all instances)
    device_type = "Smartphone"
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("phone details")
        print(f"device type {self.device_type}")
        print(f"brand type {self.brand}")
        print(f"model {self.model}")
        print(f"price {self.price}")
    def updateprice(self,price):
        self.price=price
        print("price updated")
        self.display()

p1=Phone("mi","A12",12000)
p1.display()
p1.updateprice(15000)