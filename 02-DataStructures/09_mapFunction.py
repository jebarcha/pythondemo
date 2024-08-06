items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Transform or map our original list into a different list
# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# another more elegant way: we have the map function
# x = map(lambda item: item[1], items)
# print(x)  # result: <map object at 0x000001D024AD9A80>
# for item in x:
#     print(item)

# conver the map object into a list object
prices = list(map(lambda item: item[1], items))
print(prices)

# so this is how the map function works.
# it takes a lambda function, and applies it on every item of this iterable.
