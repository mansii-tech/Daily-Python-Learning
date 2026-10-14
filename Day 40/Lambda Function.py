'''
LAMBDA FUNCTION:
lambda function in python,anonymous functions defined using the lambda keywords

Syntax: lamda arguments:expression
'''

#Basic lambda function: A simple lambda function to add two number.
add=lambda x,y : x+y
print(add(2,3))

sub=lambda a,b : a-b
print(sub(5,2))

mul=lambda x,y : x*y
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
result = mul(n1,n2)
print(f"multiplication : {result}")


#Square of a number
sq=lambda x:x**2
n1=int(input("Enter number 1"))
result = sq(n1)
print(f" Square of a number : {result}")