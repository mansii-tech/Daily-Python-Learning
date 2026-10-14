#passing tuple to a function 
def calculate(m):     #in this we can only take/retuen one value
    print(type(m))
    sum=0
    for i in m:
        sum += 1
    print(f"total marks",sum)
#passing tuple to a function
m1=int(input("enter marks"))
m2=int(input("enter marks"))
m3=int(input("enter marks"))
marks=(m1,m2,m3)
calculate(marks)              #passing tuple to a function


#variable-length argument(*args)
def calculate(*args):     #in this we can take/retuen more than one value
    sum=0
    for i in args:
        sum += i
    print(f"total marks",sum)
#passing tuple to a function
m1=int(input("enter marks"))
m2=int(input("enter marks"))
m3=int(input("enter marks"))
calculate(m1,m2,m3)


#function returning a tuple
def calculate(r):
    area=3.14*r*r
    circle=2*3.14*r
    ci=(area,circle)   #Tuple
    return ci
radius=int(input("enter radius"))
result=calculate(radius)
print(f"area of circle : {result[0]}")
print(f"circumferance of circle : {result[1] :.2f}")


