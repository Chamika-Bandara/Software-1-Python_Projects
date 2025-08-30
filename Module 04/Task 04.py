import random
random_number = random.randint(1,10)

while True:
    guess_number = int(input("Guess the number (1-10): "))

    if guess_number == random_number:
        print("Correct!")
        break
    elif guess_number < random_number:
        print("Too low!")
    else:
        print("Too high!")
