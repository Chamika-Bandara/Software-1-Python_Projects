class Car:
    def __init__(self, new_registration_number, new_max_speed):
        self.registration_number = new_registration_number
        self.max_speed =new_max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, new_speed_change):
        self.current_speed += new_speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, new_hours):
        self.travelled_distance += self.current_speed * new_hours

class ElectricCar(Car):
        def __init__(self, registration_number, max_speed, new_battery_capacity):
            super().__init__(registration_number, max_speed)
            self.battery_capacity = new_battery_capacity

class GasolineCar(Car):
        def __init__(self, registration_number, max_speed, new_tank_volume):
            super().__init__(registration_number, max_speed)
            self.tank_volume = new_tank_volume