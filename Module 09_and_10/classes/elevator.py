class Elevator:
    def __init__(self, new_bottom_floor, new_top_floor):
        self.bottom_floor = new_bottom_floor
        self.top_floor = new_top_floor
        self.current_floor = new_bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        print(f"Moving elevator to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}")