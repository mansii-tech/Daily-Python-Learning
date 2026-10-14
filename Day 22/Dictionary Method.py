#popitem
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1=patient.popitem()  #return last key value and removes it from dict.
print("pop item",p1)
print("remaining item")

#update
patient={"id":111,"name":"ravi","doctname":"mahesh"}
print(patient)
p1={"doctname":"sanskar","mobile":98989898989}
patient.update(p1)
print(patient)


#Example:-
patient={}
#adding a new key value pair to dictionary
pid=int(input("Enter patient id"))
patient["id"]=pid
pn=input("Enter patient name")
patient["name"]=pn
#display the patients
print("Patient details")
print(patient)
id=input("Enter key to update")
val=input("Enter value")
patient.update({id:val})
print(patient)

#clear

#copy
tempadd={"area":"sadar","city":"nagpur"}
permadd=tempadd.copy()  #creates a duplicate copy of distionary
print(permadd)







