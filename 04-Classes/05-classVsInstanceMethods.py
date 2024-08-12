class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x  # x and y are instance attributes
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"

# point = Point(0, 0)
point = Point.zero()  # its like a Factory Method
point.draw()  # Point (0, 0)
