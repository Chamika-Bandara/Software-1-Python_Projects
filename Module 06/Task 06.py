import math

def pizza_unit_price(diameter_cm: float, price_eur: float) -> float:
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * (radius_m ** 2)
    return price_eur / area_m2

d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (eur): "))
d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (eur): "))

u1 = pizza_unit_price(d1, p1)
u2 = pizza_unit_price(d2, p2)

print(f"\nPizza 1 unit price: {u1:.2f} eur/m2")
print(f"Pizza 2 unit price: {u2:.2f} eur/m2")

if u1 < u2:
    print(f"Pizza 1 is better value")
elif u2 < u1:
    print(f"Pizza 2 is better value")
else:
    print(f"Pizza 1 is better value")