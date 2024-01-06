# numbers
age = 12
area = 34.5
balance = 100.50

print(age)
print(balance)
print("Balance is of type: ", type(balance))

# strings and chars
first_name = "Bernard"
c = 'D'
print(first_name)
print(c)
print(first_name[2])

# Booleans
isOpen = True
isClosed = False


def check_status():
    if age > 18:
        print("Can vote")
    else:
        print("Too young to vote")


check_status()

def print_age(age):
    print("Jackon is " + str(age) + " years old")

print_age(age)
