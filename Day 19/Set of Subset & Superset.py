#subset(matching valuse=true if values is different=false)
#superset
course1={"java","php","python","oracle","html"}
course2={"php","html"}
result=course2<=course1 #subset
print(result)
result=course1>= course2#superset
print(result)

#(set) in add method
#add 3 course in set
course=set()
for i in range(3):
    c=input("Enter course name")
    course.add(c)
    print("course added to set")
print("course available")
print(course)

#remove
c=input("Enter course to remove")
course.remove(c)
print("course removed from set")
print("courses available")
print(course)


#discard
c=input("Enter course name to discard")
course.discard(c)
print("course discard from set")
print("course available")
print(course)


#difference between remove and discard
#remove give keyerror
#discard is not gives error

#POP FUNCTION(pickup random one from and give as output)
c=course.pop()
print("course popped",c)
print("course set")
print("course available")
print(course)

#Q  patient






























