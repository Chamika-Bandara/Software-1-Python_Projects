import random

def roll_d6():
    return random.randint(1, 6)

while True:
    r = roll_d6()
    print(r)
    if r == 6:
        break