from classes.car import ElectricCar, GasolineCar

ElectricCar1 = ElectricCar("ABC-15", 180, 52.5)
GasolineCar1 = GasolineCar("ACD-123", 165, 32.3)


ElectricCar1.accelerate(120)
GasolineCar1.accelerate(120)

ElectricCar1.drive(3)
GasolineCar1.drive(3)

print(f"Electric Car {ElectricCar1.registration_number} travelled: {ElectricCar1.travelled_distance} km")
print(f"Gasoline Car {GasolineCar1.registration_number} travelled: {GasolineCar1.travelled_distance} km")