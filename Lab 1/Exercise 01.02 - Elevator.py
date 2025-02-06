"""Elevator"""

class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        self.current_floor = floor

    def report_current_floor(self):
        print(self.current_floor)

def main():
    """main function"""
    max_floor = int(input())
    elevator_1 = Elevator(max_floor)

    while True:
        want_floor = input()

        if want_floor == "Done":
            Elevator.report_current_floor(elevator_1)
            return

        if int(want_floor) > max_floor:
            print("Invalid Floor!")
            continue

        Elevator.go_to_floor(elevator_1, int(want_floor))

main()
