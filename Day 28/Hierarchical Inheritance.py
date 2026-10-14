'''Hierarchical Inheritance'''

class Account:
    def __init__ (self,act_no,bal):
        self.act_no=act_no         #child class
        self.bal=bal               #child class
    def show_balance(self):
        return f"balance is {self.bal}"
    
class Saving(Account):    #two child class has a same parent class (Account)
    interest=500
    def deposit(self,amount):
        self.bal=self.bal+amount+self.interest
        return f"amount deposited with interest, bal is {self.bal}"

class Current(Account):    #two child class has a same parent class (Account)
    def deposit(self,amount):
        self.bal=self.bal+amount
        return f"amount deposited with interest, bal is {self.bal}"
    
s=Saving(44,1,00,000)
print(s.deposit(1000))
print(s.show_balance())

c=Current(44,1,00,000)
print(c.deposit(500))
print(c.show_balance())