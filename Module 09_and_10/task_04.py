from classes.car import Car
from tabulate import tabulate
import random


cars = []
for i in range(10):
    registration_number = f"ABC-{i+1}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration_number, max_speed))

race_ongoing = True
hour = 0

while race_ongoing:
    hour+=1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance>= 10000:
            race_ongoing = False
            break


table_data = []
for car in cars:
    table_data.append([
        car.registration_number,
        f"{car.max_speed} km/h",
        f"{car.current_speed} km/h",
        f"{car.travelled_distance:,.1f} km"
    ])
headers = ["Registration", "Max Speed", "Current Speed", "Travelled Distance"]
print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))