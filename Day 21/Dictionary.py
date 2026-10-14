#dictionary to store current_user(id,name,role)
current_user={"id":123,"name":"manisha","role":{"admin","customer"}}
print(current_user)
print("current user details")
print(f"id:{current_user['id']}")
print(f"name:{current_user['name']}")
r=current_user['role']#set
r1=list(r)#converting set to list
print(f"role 1:{r1[0]}")
print(f"role 2:{r1[1]}")


# dictionary methods
#1) keys function
#keys()return a view of all keys values and item in a from of tuple
#converting set into list
current_user={"id":123,"name":"manisha","role":{"admin","customer"}}
print("keys",current_user.keys())
print("values",current_user.values())
print("items",current_user.items())
print("get",current_user.get("id"))




















