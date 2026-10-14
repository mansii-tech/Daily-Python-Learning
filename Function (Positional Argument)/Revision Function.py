#Create a function calculate having 3 argument
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    else:
        print("Invalid Operator")
    print("result",result)
    return result
num1=int(input("Enter 1st Number"))
num2=int(input("Enter 2st Number"))
operator=input("Enter +,-")
calculate(num1,num2,operator)