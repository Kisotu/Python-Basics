# for loop
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days:
    print(day)

first_name = "Kabati"

# prints letters of the string
for letter in first_name:
    print(letter)

# range
# range(stop) -> generates a range from 0 up to, but not including, stop
# range(start, stop) -> generates a range from start up to, but not including, stop
# range(start, stop, step)  ->  generates a range from start to stop, incrementing by step

# print 0 - 10

print("Values of x 0 - 10")
for x in range(11):
    print(x)


# print 3 - 20

for i in range(3, 21):
    print(i)


# print 10 - 30 incrementing by 4
print("******************")
for y in range(10, 31, 4):
    print(y)
