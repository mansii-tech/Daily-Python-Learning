#-------Extend-------
'''
names1=["amit","ravi"]
print("list of name")
print(names1)
names2=["monali","radhika"]
names1.extend(names2)
print("list after extending")
print(names1)
'''
'''
#-----insert----
names1=["amit","ravi"]
print("list of name")
n=input("enter name")
names1.insert(1,n)
print(names1)
'''
'''
#------remove----
names1=["amit","ravi","manish"]
print("list of name")
n=input("enter name")
names1.remove(n)
print(names1)
'''
'''
#----pop----
#remove and return the item
names1=["amit","ravi","manish"]
print("list of name")
n=names1.pop(1)
print("name at index 1 is ",n)
print("names after pop method")
print(names1)
'''
'''
#-----index----
names1=["amit","ravi","manish"]
print("list of name")
n=names1.index("ravi")
print("index of ravi is ",n)
'''
'''
#-----count----
names1=["amit","ravi","manish","ravi"]
print("list of name")
n=names1.count("ravi")
print("count of ravi in list ",n)
'''
'''
#----sort-----
names1=["amit","ravi","manish","ravi","amita","babita","dhruvi"]
print("list of name")
names1.sort()
print("after sorting")
print(names1)
'''
'''
#----reverse---
names1=["amit","ravi","manish","ravi","amita","babita","dhruvi"]
print("list of name")
names1.sort(reverse = True)
print(names1)

#----length----
names1=["amit","ravi","manish","ravi","amita","babita","dhruvi"]
print("list of name")
names1.sort(key=len)
print(names1)

names1=["amit","ravi","manish","ravi","amita","babita","dhruvi"]
print("list of name")
names1.reverse()
print(names1)
'''
'''
#----clear----
names1=["amit","ravi","manish","ravi","amita","babita","dhruvi"]
print("list of name")
names1.clear()
print(names1)
'''
names=[]#empty list
print("select a choice")
print("1- add student name")
print("2- exit")
choice=int(input("Enter choice number"))
while(True):
    print("select a choice")
    print("1- add student name")
    print("2- exit")
    choice=int(input("Enter choice number"))
    
    if choice==1:
         name=input("enter student name")
         names.append(name)
         print("name added to list")
    elif choice==2:
        break
print("list of students")
print(names)







