list1 = [1, 2, 3]
list2 = [10, 20, 30]

# combine those 2 list into a single list
# [(1, 10), (2, 20), (3, 30)]
# we can use the built-in zip function
# print(zip(list1, list2)) # <zip object at 0x000001E4094B3900>
print(list(zip(list1, list2)))  # [(1, 10), (2, 20), (3, 30)]

# something cool, if we add "abc" it will be spread accross multiple tuples in the list
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))
