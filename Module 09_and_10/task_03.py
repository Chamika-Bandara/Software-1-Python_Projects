from classes.car import Car

car1 = Car('ABC-123', 142)
car1.accelerate(60)
car1.drive(3)

print(f'Registration: {car1.registration_number}'
      f'\nMax speed: {car1.max_speed} km/h'
      f'\nCurrent speed: {car1.current_speed} km/h'
      f'\nTravelled distance from current speed: {car1.travelled_distance} km')
