#1.Customer Segment (Data Analyst Style)
#Situation:
#Classify customers based on total spend:
#Spend ≥ 50000 → Premium
#Spend ≥ 20000 → Gold
#Spend ≥ 5000 → Silver
#Below 5000 → Bronze
spend = float(input("Enter total spend: "))
if spend >= 50000:
    segment = "Premium"
elif spend >= 20000:
    segment = "Gold"
elif spend >= 5000:
    segment = "Silver"
else:
    segment = "Bronze"
print("Customer Segment:", segment)


# 2.Leap Year Checker
# Situation:
# A year is a leap year if:
# Divisible by 4, and
# If divisible by 100, it must also be divisible by 400.
year = int(input("Enter year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


#3.Odd or Even Number
#Situation:
#Check whether a number is Odd or Even.
#Solution:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    

#4.Positive, Negative or Zero
#Situation:
#Check if a number is Positive, Negative, or Zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
    
    
#5.Largest of Two Numbers
#Situation:
#Find the largest number between two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both numbers are equal")
    
