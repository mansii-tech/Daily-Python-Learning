#dictionary popitem method
#pop item method(last ki value lega as output in pop method and remove karega divtionary se)
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1=patient.popitem()
print("pop item",p1)
print('remaining',patient)

#update method(update the value in dictionary)
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1={"doctname":"sanskar","mobile":"789328362"}
patient.update(p1)
print(patient)




#give the user input and update the value
patient={}
#adding the new key value pair to dictionary
pid=int(input("Enter patient id"))
patient["id"]=pid
pn=input("Enter patient name")
patient["name"]=pn
#display the patients
print("patient details")
print(patient)
id=input("Enter key to update")
val=input("Enter value")
patient.update({id:val})
print(patient)


#copy method
tempadd={"area":"sadar","city":"nagpur"}
permadd=tempadd.copy()#creat a duplicate copy of dictionary
print(permadd)


#exaple
stud={}
for i in range(3):
    name=input("Enter name")
    math=int(input("Enter maths"))
    chem=int(input("Enter chem"))
    stud[name]={"math":math,"chem":chem}
print(stud)    













