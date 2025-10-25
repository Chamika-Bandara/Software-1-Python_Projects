import random
from tabulate import tabulate

class Race:
    def __init__(self, name, new_distance, cars):
        self.name = name
        self.distance = new_distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        headers = ["Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Distance Travelled (km)"]
        table_data = [
            [
                car.registration_number,
                car.max_speed,
                car.current_speed,
                round(car.travelled_distance, 1)
            ]
            for car in self.cars
        ]

        print(f"\nRace Status: {self.name}")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)