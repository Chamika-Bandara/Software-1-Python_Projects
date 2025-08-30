numbers = []

while True:
    user_input = (input("Enter a number(empty to quit):"))
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input, please enter a number")

if numbers:
    print(f"Smallest number is: {min(numbers)}")
    print(f"Largest number is: {max(numbers)}")
else:
    print("No numbers entered")