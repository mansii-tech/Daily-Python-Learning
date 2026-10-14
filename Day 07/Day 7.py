#accept price number or not
num=int(input("enter number"))   #5
for i in range(2,num) :
    if num % i == 0 :
        print("num is not prime number")
        break
#check if num is not divided by any between number
if num == (i+1) :
    print("num is prime no")
    
    
#program to print prime no. between 1 and 20
for num in range(1,21):
    for i in range(1,num):
        if num % i == 0:
            print(f"{num} is not a prime no.")
            break
        if num == (i+1):
            print(f"{num} is prime no")
            
            
#calculate simple interest over time
principal=1000.0
rate=0.05
years=4
#loop througth each year from 1 to 4
for year in range (1, years + 1) :
    interest=principal*rate
    principal += interest
    print(f"Year {year} :  Balance=${principal: .2f}")
