#accesing from dictionary through key
n=input("Enter name")
a=int(input("Enter age"))
c=input("Enter city")
#using construction
student=dict(name=n,age=a,city=c)
print("student details")
print(f"name:{student['name']}")
print(f"age:{student['age']}")
print(f"city:{student['city']}")

#diffreent bet
#square bracket and get method
#suqare bracket(raises the keyerror )
#get method(not raises the error if value is not present then the get method give neno)
n=input("Enter name")
a=int(input("Enter age"))
c=input("Enter city")
#using constructor
student=dict(name=n,city=c,age=a)
print("student details")
print(f"name:{student['name']}")
print(f"age:{student['age']}")
print(f"city:{student['city']}")

#assingment:
#create a dictionary named product to store product_id, product_name
#price and stock. accept from user and store it in dictionary then display using
#([] bracket and get method)
p1=input("Enter product id")
p2=input("Enter product name")
p3=int(input("Enter product price"))
p4=input("Enter product stock")
product=dict(product_id=p1,product_name=p2,product_price=p3,product_stock=p4)
print("product details")
print(f"id:{product['product_id']}")
print(f"name:{product['product_name']}")
print(f"price:{product['product_price']}")
print(f"stock:{product['product_stock']}")

























