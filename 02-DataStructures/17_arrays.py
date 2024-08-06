from array import array

numbers = array("i", [1, 2, 3])
# print(numbers) # array('i', [1, 2, 3])

# similar to list we have methods to add like append and insert
# numbers.append(4)  # add a number at the end of the array
# numbers.insert()  # add a number to a specific index

# exactly like list we have pop and remove
# numbers.pop()
# numbers.remove(4)

# unlike lists, the object in the array are typed.
# that means that each item should be int
# numbers[0] = 1.0 # error because is of different type
