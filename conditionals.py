import random
import math
''' this is used for multiple line
comments'''

number = 1
if number > 2:
    print(f"{number} is greater than 2")
else:
    print(f"{number} is less than 2")

number2 = random.randint(10, 1000)

# valid if number2 is above 45 and the last digit is not 0
if number2 > 45 and number2 % 10 != 0:
    print(f"{number2} is greater than 3 and the last digit is not 0")

print("The value of pi is", math.pi)
# list literal
colors = ["red", "blue", "yellow"]
print(colors)

# tuple literal
numbers = (1, 3, 5, 6)
print(numbers)
