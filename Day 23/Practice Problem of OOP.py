#create a class customer having attributes cust_id,cust_name,cust_email,cust_mobile
class customer:
    cust_id=None
    cust_name=None
    cust_mail=None
    cust_mobile=None
c=customer()
c.cust_id=input("Enter Customer ID")
c.cust_name=input("Enter Customer Name")
c.cust_mail=input("Enter Customer Email")
c.cust_mobile=int(input("Enter Mobile Number"))
print("Customer Details")
print(f"cust_id : {c.cust_id}")
print(f"cust_name : {c.cust_name}")
print(f"cust_mail : {c.cust_mail}")
print(f"cust_mobile : {c.cust_mobile}")

#create a class patient having attr. pat_id,name,disease,doctorname
