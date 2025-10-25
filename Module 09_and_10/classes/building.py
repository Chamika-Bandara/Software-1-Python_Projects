from elevator import Elevator

class Building:
    def __init__(self, new_bottom_floor, new_top_floor, number_of_elevators):
        self.bottom_floor = new_bottom_floor
        self.top_floor = new_top_floor
        self.elevators = [Elevator(new_bottom_floor, new_top_floor) for _ in range(number_of_elevators)]
        print(f"Building created with {number_of_elevators} elevators.\n")

    def run_elevator(self, elevator_number, target_floor):
        if 1 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
            elevator = self.elevators[elevator_number - 1]
            elevator.go_to_floor(target_floor)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("\nFIRE ALARM! Moving all elevators to bottom floor")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Moving elevator {i} to bottom floor.")
            elevator.go_to_floor(elevator.bottom_floor)