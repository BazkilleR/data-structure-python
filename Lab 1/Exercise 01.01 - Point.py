"""Point"""

class Point:
    def __init__(self, x=0, y=0):
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def calculate_distance(self, other_point):
        return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2) ** 0.5

if __name__ == "__main__":
    """main function"""
    p1 = Point(float(input()), float(input()))
    p2 = Point(float(input()), float(input()))
    result = Point.calculate_distance(p1, p2)
    print(f"{result:.2f}")
