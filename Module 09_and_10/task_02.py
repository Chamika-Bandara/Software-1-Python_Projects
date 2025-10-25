from classes.car import Car

car1 = Car('ABC-123', 142)

print(f'Registration: {car1.registration_number}'
      f'\nMax speed: {car1.max_speed} km/h'
      f'\nCurrent speed: {car1.current_speed} km/h'
      f'\nTravelled distance: {car1.travelled_distance} km')

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f'Speed after total acceleration: {car1.current_speed} km/h')

car1.accelerate(-200)

print(f'Final speed after hitting emergency brake: {car1.current_speed} km/h')