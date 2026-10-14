'''OOP (Object Oriented Programmming)
attribute
method
Bacis Concepts:- Class,Object,Attributes,Methods,Function
'''

#Create a class book  
class Book:
    title="Python Notes"   #title,author,class is attribute
    author="Mansi"
    price=1200
b=Book() #creating object
print(b.title)

#Create a class book  
class Book:
    title=None   #title,author,class is attribute
    author=None
    price=0
b=Book()         #creating object
print("Enter Book Details")
b.title=input("Enter Title")
b.author=input("Enter Author Name")
b.price=int(input("Enter Price"))
print("Book Details")
print(f"title:{b.title}")
print(f"author:{b.author}")
print(f"price:{b.price}")

#create a class customer having attributes cust_id,cust_name,cust_email,cust_mobile
#create a class patient having attr. pat_id,name,disease,doctorname