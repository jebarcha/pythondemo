# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()  # ->will not modify the original list, it will return a new sorted list.

# print(sorted(numbers))  # ->will create a new list: [2, 3, 6, 8, 51]
# print(sorted(numbers, reverse=True))

# print(numbers)  # [3, 51, 2, 8, 6]

# # numbers.sort(reverse=True)
# # print(numbers)

# -----------------------------
# deal with complex objects
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
