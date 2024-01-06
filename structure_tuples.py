# Tuples - ordered sequence of items but immutable. enclosed by () parentheses

product = ("Xbox", 245.55, "2021", "USA", [23, 4, 56, "Hello"])

print(product[0])
print(product[:3])

print(len(product))

for item in product:
    print(item)

inside_list = product[4]
inside_list.append(3)

print(product)

print(" ")
for x in inside_list:
    print(x)
