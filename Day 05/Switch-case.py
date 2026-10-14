'''
Switch Case
'''

#accept dayno and print dayname using match statement
dayno=int(input("enter dayno(1-7)"))
match dayno :
    case 1 :
        print("monday")
    case 2 :
        print("tuesday")
    case 3 :
        print("wednsday")
    case _:
        print("some other day")
        

#accept character and print vowel or not
ch=input("Enter Character")
match ch :
    case 'a' | 'e' | 'i' | 'o' | 'u' :         #| :- pipe character
        print("vowel")
    case _:
        print("Not a vowel")
        
        
#accept 2 numbers and operator and print result using match
n1=int(input("enter number 1"))
n2=int(input("enter number 2"))
op=input("enter operator")
match op :
    case '+' :
        result = n1+n2
    case '-' :
        resule = n1-n2
    case '*' :
        result = n1*n2
    case '%' :
        result = n1%n2
    case _:
        print("not a valid operator")
print(f"result : {result}")
       
        
#accept score and print grade       
score=int(input("enter score"))
match score:
    case s if s>=90 and s<=100 :
        print("Grade A")
    case s if s>=80 :
        print("Grade B")
    case s if s>=70 :
        print("Grade  C")
    case s if s>=0 :
        print("Fail")
    case _:
        ptint("invalid")


#accept age and print whether old,young or child.
#accept sales_amount and print whether  eligible to get discount or not.