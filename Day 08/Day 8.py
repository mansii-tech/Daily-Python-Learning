#wap to print number from 1 to 5 using while loop
i=1
while i<=5 :
    print(i)
    i += 1
    
    
#wap to print number from 1 to 5 using while loop
i=1
while True:
     print(i)
     i += 1
     if i>10:
         break
print("bye")


#wap to print 5to 20
i=5
while i<=20 :
   print (i)
   i +=1
   
#wap to print 2 to 30
i=2
while i<=30 :
 print(i)
 i += 2
 
#wap t accept a number and print factorialwhile True:
while True:
    num=int(input("enter number"))
    fact=1
    while num>0:
        fact=fact*num
        num -=1
    print(f"fact:{fact}")
    ans=input("do you want to continue, pess yes or no").lower()
    if ans=="no" :
        break
print("bye")


#wap to accept password
password=input("enter password")#Abc@123
isdigit=False
isspecial=False
special="!@#%"
if len(password) >= 8:
    for p in password:
        if p.isdigit():
            isdigit=True
        elif p in special:
            isspecial=True
    if isdigit==True and isspecial==True:
        print("password is valid")
    else:
        print("invalid password")
else:
    print("password should be atleast 8 charcters")