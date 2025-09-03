def gallons_to_liters(gal: float) -> float:
    return gal * 3.785411784

while True:
    g = float(input("Enter gallons (negative to quit):"))
    if g < 0:
        print("Bye!")
        break
    print(f"{g} gallon(s) = {gallons_to_liters(g): .3f} liters")
