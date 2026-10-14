'''
Exception Handling:
Error coming when you run the program is call Exception Handling
So Exception Handling machanism will handle the error and program will successfully run till the end.
Inside this has try,except,finally and raise keywords are used to handle run time error

Try: in try block you will write the code where chances of error occur
Except: except block will handle the error which is thrown by try block
'''

n1=10
n2=0
result=0
try:
    result=n1/n2   #Error will come if n2 is zero it will caught by except block
    print(res)
except ZeroDivisionError as e:
    print(f'error:{e}')
print(f'result:{result}')
print("bye")


#Program 1 : Handle division by zero
try:
    num1=int(input("Enter numerator:"))
    num1=int(input("Enter dinominator:"))
    result = num1/num22
    print(f'result:{result}')
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
print("bye")
   

#Program 2:
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError as e:
    print(e)
    print("try again")
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
print("bye")
    
    
    
    
    
    


