import random

balance = 500.65
# if, elif, else
if balance < 500:
    print("Ypu cannot withdraw")
elif balance > 500:
    print("You can withdraw")
else:
    print("Cannot execute operation, seek customer care")

# while loop
# print 0 - 15
i = 0

while i <= 15:
    print(i)
    i = i + 1

print("**********")
# while loop
# print odd numbers between 10 and 50
k = 10
while k <= 50:
    if k % 2 != 0:
        print(k)
    k = k + 1

