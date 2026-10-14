'''
MODULE:
Module is a python file which contains functions,classes and variables.
Which can be resused in any python program.

TYPES OF MODULE:
1.Build-In Module (math,random,os)
2.Third Party Modules (pandas,numpy,scikit-learn,pytorch)
3.User Defined Module (Custom Module)
'''

#Build-In Example:- math
#1st way
import math #math is build-in module
print(math.pi)
print(math.sqrt(20))
print(math.cos(0))

#2nd way
from math import pi,sqrt
print(pi)
print(sqrt(20))

#3rd way (short cut)
from math import sqrt as s,pi as p
print(p)
print(s(20))


#Build-In Example:- random
import random as r
print(r.randint(1,10))

