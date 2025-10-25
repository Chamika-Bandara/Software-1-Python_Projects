from classes.car import Car

car1 = Car('ABC-123', 142)

print(f'Registration : {car1.registration_number} '
      f'\nMax speed: {car1.max_speed} km/h' 
      f'\nCurrent Speed : {car1.current_speed} km/h' 
      f'\nTravelled Distance: {car1.travelled_distance} km')