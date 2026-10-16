'''
csv.reader()
-'''

import csv
with open ('student.csv', 'r', newline='') as file:
    read=csv.reader(file)
    print("Student Details")
    '''
    for r in read:
           print(type(r))
        print(r)
    '''
    print("--------Student Details----------")
    for r in read:
        print(f"name : {r[0]}, age : {r[1]}, salary : {r[2]}")
        
        
#Skip the First Row
import csv
with open('student.csv','r',newline='') as file:
    w = csv.reader(file)
    next(w)    #skip the first row
    for r in w:
        print(r)