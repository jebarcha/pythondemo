# numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# print(uniques)  # {1, 2, 3, 4}

# second = {1, 4}
# print(second)
# second.add(5)
# second.remove(5)
# print("len:", len(second))
# print(second)

# example of math
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# union that will contains all items from first and second set
print(first | second)  # {1, 2, 3, 4, 5}

# intersection of 2 sets
print(first & second)  # {1} -> only number that exists in both sets

# the difference between two sets
print(first - second)  # {2, 3, 4}

# simetric difference: returns the items that are either in the first or second sets, but not both.
print(first ^ second)  # {2, 3, 4, 5}

# print(first[0]) # error because sets are unordered collection and we cannot access them by index.

# check if an item exists in a set
if 1 in first:
    print("exists")
