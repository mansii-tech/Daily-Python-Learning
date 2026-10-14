'''
TUPLE:
'''

#explicit
num=(4,6.2,"Hello",True)    #explicit
print(type(num))
print(num[0])
for i in num:
    print(i)
num1=(22,)
print
    

# implicit way to denote tuple
num=1,2,4,"hello"      #implicit way to denote tuple
print(type(num))
for i in num:
    print(i)
    
    
num=1,2,4,"hello"
print(type(num))
print(num[-1])         #to get the last element of tuple [-]


'''
SLICING
'''
num=(0,1,2,3,4,5,6)
print(num)
print(num[4])
print(num[1:4])
print(num[2:])       #index 2 se baki kein element
print(num[::2])      #Gap of 2
print(num[::-1])     #Reverse the element