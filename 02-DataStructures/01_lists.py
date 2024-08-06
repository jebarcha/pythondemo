letters = ["a", "b", "c", "d"]  # a list
matrix = [[0, 1], [2, 3]]  # two dimensional list
zeros = [0] * 5  # with asteriscs repeat an item by x
# print(zeros)
combines = zeros + letters
print(combines)

# In python every item in the list can be of different type
# we can combine a list of numbers with strings, boolean or even lists

# we want: [0, 1, 2, 3... 20]
numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))
