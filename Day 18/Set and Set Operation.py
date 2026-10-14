'''SET'''

#creating set
stud={"mansi","java",222,"mansi"}
print(stud)

#Using set constructor
stud=set(["mansi","java",222,"mansi"])   #Remove duplicates
print(stud)


''' OPERATION OF SET'''

#union(|)
stud1={"rani","roshni"}
stud2={"mansi","tanu","kanha"}
stud3={"khushi","saima","vaishnavi","mayuri"}
stud=stud1 | stud2 | stud3
print("All Student List")
print(stud)

#intersection(&)
stud1={"mansi","tanu"}
stud2={"saima","mansi"}
stud=stud1 & stud2
print("Commom Student Name")
print(stud)

#Difference(-)
stud1={"mansi","tanu","mona"}
stud2={"saima","mansi"}
stud=stud1 - stud2
print("Difference Student Name")
print(stud)

days={"mon","tue","wed","thu","fri","sat"}
attendence={"tue","thu","sat"}
absent= days - attendence
print("Employee Absent On:")
print(absent)

#symmetric difference(^)
days={"mon","tue","wed","thu","fri","sat"}
attendence={"tue","thu","sat"}
absent= days ^ attendence
print("Not in Both:")
print(absent)
