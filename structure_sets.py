# sets - unordered collection of items. Indexing does not work.
# defined inside curly {} races

numbs = {1, 34, 45, 56, 6, 67, 65, 2, 9}

print(numbs)
# output does not follow defined sequence

numbs.pop()
print(numbs)

numbs.add(35)
print(numbs)

for item in numbs:
    print(item)
