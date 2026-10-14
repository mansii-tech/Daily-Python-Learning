#keyword argument
#function to calculate electricity bill
def cal_bill(cust_name,unit,rate):
    total=unit*rate
    print("bill details")
    print(f'customer name :{cust_name}')
    print(f'total amount :{total}')

cal_bill(unit=250,rate=7.5,cust_name="amitkumar")#keyword arguments


#function returning a value
#function to calculate electricity bill
def cal_bill(cust_name,unit,rate):
    total=unit*rate
    print("bill details")
    print(f'customer name :{cust_name}')
    return total

result=cal_bill(unit=250,rate=7.5,cust_name="amitkumar")#keyword arguments
print(f'total amount :{result}')


#default argument
#function to calculate electricity bill
def cal_bill(cust_name,unit,rate=5.5):
    total=unit*rate
    print("bill details")
    print(f'customer name :{cust_name}')
    return total

result=cal_bill("manish kumar",350,8.0)
print(f'total amount :{result}')

result=cal_bill("ravish kumar",350)#it will use default argument value
print(f'total amount :{result}')


