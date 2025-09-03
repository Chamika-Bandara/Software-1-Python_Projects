import random

def roll_dice(sides: int) -> int:
    return random.randint(1, sides)

sides = int(input("Enter number of sides on the die: "))
print(f"Rolling until {sides} appears....")

while True:
    r = roll_dice(sides)
    print(r)
    if r == sides:
        break

