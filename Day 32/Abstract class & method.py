'''
Abstract class & method
This is achived using the abc module(Abstract Base Class)
Syntax:-
from abc import ABC,absractmethod

Module always be in CAPITAl
Class in SMALL
'''

#Example of Abstract class and method
from abc import ABC,abstractmethod
#creating an abstract class for that you have inherit your class from ABC class
class Account(ABC):     #Abstract Class
    #creating an abstract method
    bal=1000000000
    @abstractmethod     #Decorator (@ is used for calling method)
    def deposit(self):
        pass
    
class Saving(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount+5000000
        print('Balance with interest is',self.bal)
        
class Current(Account):
    def deposit(self,amount):
        self.bal=self.bal+amount
        print('Balance without interest is',self.bal)
        
s=Saving()
s.deposit(1000000)
c=Current()
c.deposit(2000000000)