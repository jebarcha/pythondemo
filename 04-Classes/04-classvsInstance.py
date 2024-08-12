class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x  # x and y are instance attributes
        # attributes that belong to point instances or point objects.
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"

point = Point(1, 2)
# point.z = 10
print(point.default_color)
point.draw()


point2 = Point(3, 4)
print(point2.default_color)
point2.draw()
