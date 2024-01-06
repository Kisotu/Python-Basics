# is, is not -> identity operators


x = 9
y = 45
x2 = 9

if x is x2:
    print("Equal and same")
else:
    print("Not equal at all")

# in, not in -> membership operators

my_list = [12, 34, 65, 43, "Red", 98.50, "Mountain"]
k = 33
print("K = ", k)
if k in my_list:
    print("K is in the list")
else:
    print("Not in the list")

if k not in my_list:
    my_list.append(k)
    print("K added to list")
    if k in my_list:
        print(my_list)
        print("as seen here: my_list[-1] => ", my_list[-1])
