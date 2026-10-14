#LIST:
student=[12,"Mansi","Java"]
print("student details")
print(f"Roll No. :{student[0]}")
print(f"Name :{student[1]}")
print(f"Course :{student[2]}")
print("Details using for loop")
for s in student:
    print(s)


#SLICING:
weeks=["Monday","Tuesday","Wednsday","Thusday","Friday","Saturday","Sunday"]
print(weeks[1:4])
print(weeks[:4])
print(weeks[1:])
print(weeks[0:6:4])
print(weeks[::2])
print(weeks[4:1:-1])
print(weeks[::-1])

#LIST METHOD
#append(x): adds an item x to the end of the list.
student=["Rani","Tanu"]
print(student)
name=input("Enter New Name")
#add this to list
student.append(name)
print('After adding new name')
print(student)