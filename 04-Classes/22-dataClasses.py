from collections import namedtuple

# these tuples are immutables
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)  # 1
p2 = Point(x=1, y=2)
print(p1 == p2)  # True


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)  # False but with the magic method __eq__ we compare by values
# print(id(p1))  # 2178328993072
# print(id(p2))  # 2178328993024
