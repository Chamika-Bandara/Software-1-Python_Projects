from classes.car import Car
from classes.race import Race
import random


cars = []
for i in range(10):
    reg_number = f"CAR-{i+1}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))


race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
print(f"\nStarting Race: {race.name} ({race.distance} km)\n")


while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:")
        race.print_status()

print(f"\nRace finished in {hours} hours!")
race.print_status()






