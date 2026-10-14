'''ZeroDivisionError'''
n1=int(input("Enter number 1"))
n2=int(input("Enter number 2"))
try:
    result=n1/n2
    print(f"result is {result}")
except ZeroDivisionError as e:
    print(e)
else:
    print("else block will execute if error does not come")
finally:
    print("finally block execute wheather error occurs or not")
print("bye")    


'''Index Error'''
fruits=["apple","banana","cherry"]
print(fruits[0])
print(fruits[3])
print("Bye")

#without error
fruits=["apple","banana","cherry"]
try:
    print(fruits[0])
    print(fruits[3])
except IndexError as e:
    print(f"error:{e}")
print("Bye")


'''KeyError in Dictionary'''
Student={"name": "John","age":22}
print(student['name'])
print(student['age1'])
print("bye")

#without error
Student={"name": "John","age":22}
try:
   print(student['name'])
   print(student['age1'])
except KeyErroe as e:
    print?(f"key not fount in dictionary:{e}")
print("bye")



'''
1. Basic Division with ZeroDivisionError
Python
#Program 1: Handle division by zero '''
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    

'''
2. Handling ValueError in Integer Conversion
Python
# Program 2: Handle invalid input for integer'''
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Error: Please enter a valid integer!")
    
'''
3. Multiple Exceptions (ValueError + ZeroDivisionError)
Python
# Program 3: Handle multiple exceptions'''
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Division result:", result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
'''
4. Using else Block (Runs if no exception)
Python
# Program 4: Demonstrate else block'''
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered:", num)
    print("Square of number is:", num ** 2)
    
    
'''
5. finally Block (Always executes)
Python
# Program 5: Demonstrate finally'''
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed. Closing resources if any...")
    # file.close() would go here in real use
    
    
'''
6. IndexError in List Access
Python
# Program 6: Handle IndexError'''
fruits = ["apple", "banana", "cherry"]
try:
    index = int(input("Enter index (0-2): "))
    print("Fruit:", fruits[index])
except IndexError:
    print("Error: Index out of range! Please enter 0, 1, or 2.")
except ValueError:
    print("Please enter a valid integer!")


'''
7. KeyError in Dictionary
Python
# Program 7: Handle KeyError'''
student = {"name": "John", "age": 20}
try:
    grade = student["grade"]
except KeyError:
    print("Key 'grade' not found in dictionary!")
else:
    print("Grade:", grade)
    

'''
8. Generic Exception (Catch All)
Python
# Program 8: Catch any exception'''
try:
    result = 10 / int(input("Enter a number: "))
    print("Result:", result)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    

'''
9. Raising Custom Exception
Python
# Program 9: Raise exception manually'''
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"You are {age} years old.")
except ValueError as ve:
    print(f"Invalid age: {ve}")
    
    
'''
10. Custom Exception Class
Python
# Program 10: Define and use custom exception'''
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("You entered:", num)
except NegativeNumberError as nne:
    print("Error:", nne)
except ValueError:
    print("Please enter a valid number!")
 



