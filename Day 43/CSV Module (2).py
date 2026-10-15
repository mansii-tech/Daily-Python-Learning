'''
What is the csv module?
The csv module in python helps you reda file from and write to CSV files easily n correct - even when data contain commas,quotes,newlines,etc
'''

#Program to create a csv file and write the data into it.
import csv
#create or open the csv file in write mode
with open('student.csv','w',newline='') as file:
    w=csv.writer(file)
    w.writerow(['name','age','salary'])
    w.writerows([['saima',23,100000],['mansi',22,200000]])
print("csv file created successfully")


#program to create a csv file and write the data into it (User Input)
import csv
#create or open the csv file in write mode
with open('student.csv','w',newline='') as file:
    w=csv.writer(file)
    w.writerow(['Name','Age','Salary'])
    for i in range(3):
        n=input("enter name ")
        a=int(input("enter age"))
        s=float(input("enter salary"))
        w.writerow([[n,a,s]])
print("csv file created successfully")