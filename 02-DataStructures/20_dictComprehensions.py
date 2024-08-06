# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)

# list comprehension
# [expression for item in items]
# this code same result of above code:
values = [x * 2 for x in range(5)]
print(values)  # [0, 2, 4, 6, 8]

# not limited to list, can be used for set and dictionaries
valuesSet = {x * 2 for x in range(5)}
print(valuesSet)  # {0, 2, 4, 6, 8}

# difference between a set and a dictionary
# for both we use curly braces {}
# in sets we only have values {1, 2, 3, 4}
# in dictionaries we have key-value pairs separate by a colon {1: "a", 2: "b"}

# We can use comprehensive expressions to create dictionary objects
valuesDict = {x: x * 2 for x in range(5)}
print(valuesDict)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# so, we can use previous line to create a dictionary instead of this:
# values = {}
# for x in range(5):
#     values[x] = x * 2
# print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# We can use comprehensions with list, sets and dictionaries

valuesTuples = (x * 2 for x in range(5))
print(valuesTuples)  # <generator object <genexpr> at 0x0000023AA4F43780>
