#create a function display to print("hello fron itp")
def display():
    print("Hello from Itp")
    print("Im Mansi")
print("call the function display")
display()
'''
we can call function many time in one program
'''

#function square with one parameter to square the number
def square(num):     #positional argument
    sq=num*num
    return sq
num=int(input("Enter Number"))
result=square(num)
print(f"Square of number is: {result}")


#function to print factorial of a number
def factorial(num):
    fact = 1
    while (num > 0) :
        fact = fact*num



#create a function calculate with 3 parameter to accept 2no and 1 operator
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result=n1*n2
    else:
        print("invalid")
    print(f"result is - {result}")
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
operator=input("enter operator(+,-,*,/)")
calculate(num1,num2,operator)


#function to check username and password
def check(username,password):
   if username=="mansi" and password=="mansimahi" :
      print("valid")
   else:
       print("invalid")
u=input("enter username")
p=input("enter password")
check(u,p)


'''
assignment
1.function calculate with 3 argument to accept 3 sunject marks and print total and percentage and grade
2.function calculate with one argument to accept unit and calculate bill_amount
- 0-100 - 8 rs
- 101-300 - 12 rs
 > 300 -15 rs
'''
