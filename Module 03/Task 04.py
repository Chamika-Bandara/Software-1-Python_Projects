leap_year = int(input("Enter a year: "))
if leap_year % 400 == 0 :
    print(f"{leap_year} is a leap year")
elif leap_year % 100 == 0 :
    print(f"{leap_year} is NOT a leap year")
elif leap_year % 4 == 0 :
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is NOT a leap year")

