'''Encapsulation'''

#Private Attribute Example: 1
class Account:
    def __init__(self,actno,balance):
        self.actno=actno  #Public Attribute
        self.__balance=balance    #Private Attribute

a=Account(11,1000)
print(a.actno)
#print(a.balance) error
print(a._Account__balance)  #Accesing Private Attribute using name mangling


#Private Attribute & Private Method Example: 2

class Account:
    def __init__(self,actno,balance):
        self.actno=actno  #Public Attribute
        self.__balance=balance    #Private Attribute
    #Private Method
    def __showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(11,1000)
print(a.actno)
#print(a.balance) error
print(a._Account__balance)  #Accesing Private Attribute using name mangling
a._Account__showbalance()  #Name Mangling


#Private Attribute & Public Method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno  #Public Attribute
        self.__balance=balance    #Private Attribute
    #Private Method
    def __showbalance(self):
        print(f"balance is {self.__balance}")
        
a=Account(11,1000)
print(a.actno)
#print(a.balance) error
a._Account__showbalance()


#Protected Attribute & Public Method
class Account:
    def __init__(self,actno,balance):
        self.actno=actno  #Public Attribute
        self._balance=balance    #Protected Attribute

class Saving(Account):
    def showbalance(self):
        print(f"balance is {self._balance}")
        
a=Saving(11,1000)
print(a.actno)
a.showbalance()