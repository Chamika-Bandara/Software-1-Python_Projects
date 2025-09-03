import random
n = int(input("How many dice to roll?"))
total = 0
for _ in range(n):
    total +=random.randint(1,6)
print(f"Sum of {n} dice: {total}")