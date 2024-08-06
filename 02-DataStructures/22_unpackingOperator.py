# numbers = [1, 2, 3]
# print(numbers)  # [1, 2, 3]
# print(1, 2, 3)
# print(*numbers)  # similar to the spread operator in javascript. 1 2 3

# values = list(range(5))
# print(values)  # [0, 1, 2, 3, 4]
# values = [*range(5), *"Hello"]
# print(values)  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# combine multiple lists
# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# print(values)  # [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']

# to unpack dictionaries we use two **
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
# if we have same key, it will take the last value
print(combined)  # {'x': 10, 'y': 2, 'z': 1}
