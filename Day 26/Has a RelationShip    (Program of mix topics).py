'''Customer has account(has a relationship)'''

class Customer:
    def __init__(self, customer_id, name):   #Constructor
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
        
#creating a class Account
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
        
#execution of program start here    
c=Customer(123,'kashish')   #it will call customer class constructor
a=Account(1,1000)    #it will call account class constructor
c.add_account(a)
print("customer details")
print(f"customer id : {c.customer_id}")
print(f"customer name : {c.name}")

# Display account details through customer object
print(f"Account No : {c.accounts[0].account_no}")
print(f"Balance : {c.accounts[0].balance}")