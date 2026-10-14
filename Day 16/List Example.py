#program to accept names
names=[]  #empty list
print("Select your choice")
print("1- add student name")
print("2- exit")
while(True):
    choice=int(input("Enter choice number"))
    if choice==1:
         n=input("enter student name")
         names.append(n)
    elif choice==2:
        break
print("list of students added")
print(names)


#extending program to add roll no.,name and course
names=[]  #empty list
print("Select your choice")
print("1- add student name")
print("2- exit")
while(True):
    choice=int(input("Enter choice number"))
    if choice==1:
         r=int(input("Enter Roll no."))
         n=input("Enter student name")
         c=input("Enter Course name")
         stud=(r,n,c)   #make tuple but we also use as a list also
         names.append(stud)
    elif choice==2:
        break
print("list of students added")
print(names)

#and extendind more
names=[]  #empty list
print("Select your choice")
print("1- add student name")
print("2- exit")
while(True):
    choice=int(input("Enter choice number"))
    if choice==1:
         r=int(input("Enter Roll no."))
         n=input("Enter student name")
         c=input("Enter Course name")
         stud=(r,n,c)   #make tuple but we also use as a list also
         names.append(stud)
    elif choice==2:
        break
print("list of students added")
for i in names:
    print(i)
    print(f"Roll no.:{i[0]}")








