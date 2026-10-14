#example of keyword arguments
def calculate(n1,n2,op):
    result=0
    if op=='+':
        result=n1+n2
    elif op==


#example of default argument
def contact(fullname,phonenumber,city="Nagpur"):
    print("----Contact Details----")
    print(f"Fullname:{fullname}")
    print(f"Phone Number:{phonenumber}")
    print(f"City:{city}")
#ACCEPT DETAILS
fn=input("Enter Your Fullname")
ph=input("Enter Phone Number")
ch=input("Yon want to add City")
if ch=="YES":
    c=input("Enter Your City")
    contact(fn,ph,c)
else:
    contact(fn,ph)


#function having variable length argument for fees
def cal_fees_amount(*args):
    l=len(args)
    total=0
    for i in range(l):
        total=total + args[i]
    return total

amount1=float(input("enter amount 1:"))
amount2=float(input("enter amount 2:"))
amount3=float(input("enter amount 3:"))
ta=cal_fees_amount(amount1,amount2,amount3)
print(f"total fees amount paid :{ta} Rs.")

