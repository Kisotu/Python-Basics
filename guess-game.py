import random

# Guessing game that counts the no of iterations it takes to reach a target answer
target = 32
counter = 0

while True:
    counter += 1
    random_val = random.randint(10, 50)

    print(f"Trying {random_val}...")
    if random_val == target:
        break

print(f"It took {counter} tries to arrive at {target}")
