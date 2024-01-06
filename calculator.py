def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def product(a, b):
    return a * b


def division(a, b):
    return a / b


a = 10
b = 5

user_choice = input("Enter choice (add, sub, mut, div ): ")


def calc(user_choice):
    if user_choice == "add":
        print("Addition result is: ", addition(a, b))
    elif user_choice == "sub":
        print("Subtraction result is: ", subtraction(a, b))
    elif user_choice == "div":
        print("Division result is: ", division(a, b))
    elif user_choice == "mut":
        print("Multiplicaion result is: ", product(a, b))
    else:
        print("Invalid choice")

calc(user_choice)