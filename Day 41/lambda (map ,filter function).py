'''
LAMBDA FUNCTION USING MAP FUNCTION
syntax: map(function,iterable)
'''
#Example of map function
res = lambda n : n*n
num = [1,2,3]
result = list(map(res,num))
print(result)


#Lambda Function to add corresponding elements from two lists (pass two arrgument)
numbers1=[1,2,3]
numbers2=[4,5,6]
result=list(map(lambda x, y:x + y, numbers1, numbers2))
print(result)


'''FILTER FUNCTION
syntax: filter(function,iterable)'''

#filter even number from iterable
num=[1,2,3,4,5,6,7,8]
result=list(filter (lambda x : x%2==0, num))
print(result)

#filter odd number from iterable
num=[1,2,3,4,5,6,7,8]
result=list(filter (lambda x : x%2!=0, num))
print(result)


'''sorted() function
is used to sort an iterable and return a new sorted list.

sort(iterable, key=none, reverse=false)'''

#list.sort() (filter even number from iterable)
num=[11,2,3,4,15,6,7,8]
print(f"before sorting : {num}")
num.sort()
print(f"after sorting : {num}")

#sorted()
numbers=[5,2,8,1,9]
sorted_numbers = sorted(numbers)
print(f"numbers : {numbers}")
print(f"after sorting : {sorted_numbers}")


#DECENDING ORDER
numbers=[5,2,8,1,9]
sorted_numbers = sorted(numbers, reverse=True)
print(f"numbers : {numbers}")
print(f"after sorting : {sorted_numbers}")
