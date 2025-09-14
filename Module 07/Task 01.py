seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("enter the number of a month (1-12):"))

if month in (12, 1, 2):
    print(seasons[0])
elif month in (3, 4, 5):
    print(seasons[1])
elif month in (6,7,8):
    print(seasons[2])
elif month in (9,10,11):
    print(seasons[3])
else:
    print("Invalid month number! Please enter 1-12")
