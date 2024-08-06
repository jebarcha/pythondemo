# point = 1  # <class 'int'> not a tuple but an int
# point = 1, # <class 'tuple'>
# point = () # an empty tuple
# point = 1, 2  # or (1, 2)
# print(type(point))  # <class 'tuple'>

# we can concatenate two tuples (similar to list)
# point = (1, 2) + (3, 4)
# print(point)  # (1, 2, 3, 4)

# use the * to repeat
# point = (1, 2) * 3
# print(point)  # (1, 2, 1, 2, 1, 2)

# convert a list to a tuple with the tuple function
# point = tuple([1, 2])
# print(point)  # (1, 2)

# words = tuple("Hello")
# print(words) # ('H', 'e', 'l', 'l', 'o')

# access using the index
point = (1, 2, 3)
print(point[0])  # 1

# access a range of items
point = (1, 2, 3)
print(point[0:2])  # (1, 2)
x, y, z = point
print(x)  # 1

# check existance of an item
if 10 in point:
    print("exists")

# point[0] = 10  # error because tuples are immutable, we cannot change them

# use cases: when we have a list of items and we don't want to accidentally modify this sequence
# we don't want accidentally add new items on it or remove existing one.
