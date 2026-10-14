#A variable's type can change during execution by assigning a new value of a different type.
num=20
print(type(num))
num=20.9
print(type(num))
num="hello"
print(type(num))

#multiple variable in one line
n1,n2,n3=10,20,30
print(f"num1 : {n1}, num2 : {n2}, num3 : {n3}")

#Type Conversion
n1="12"            #<string>
n2="33.3"
result=int(n1) + float(n2)  #converting
print(f"result : {result}")


#converting input to boolean
is_student=input("Are you a student? (yes/no): ").lower()=="yes"
print ("Student status:",is_student)

#(if input is yes) or direct you want to type true or false
is_active=bool(input("enter true or false for is_active"))
print("is_active")

#accept multiple inputs
#Split input string to accept multiple values.
n1,n2,n3=input("Enter three numbers(seperated by space):").split()
print(f"n1={n1}, n2={n2}, n3={n3}")
total=int(n1) + int(n2) + int(n3)
print(f"total:{total}")