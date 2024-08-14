import numpy as np

# array = np.array([1, 2, 3])
# print(array)
# print(type(array))  # <class 'numpy.ndarray'>

# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)
# print(type(array))  # <class 'numpy.ndarray'>
# print(array.shape) # tuple of (2, 3)


# array = np.zeros((3, 4), dtype=int)
# print(array)


# array = np.ones((3, 4), dtype=int)
# print(array)


# array = np.full((3, 4), 5, dtype=int)
# print(array)

# ------------
# array = np.random.random((3, 4))
# print(array)
# print(array[0, 0])

# array[0][0]
# print(array > 0.2)

# print(array[array > 0.2])

# print(np.sum(array)) # sum of values of the array

# print(np.floor(array))

# print("ceil:", np.ceil(array))

# print("round:", np.round(array))

# -------------------
# first = np.array([1, 2, 3])
# second = np.array([1, 2, 3])
# print(first + second)  # [2 4 6]
# print(first + 2)  # [3 4 5]

# -------------------
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)  # [2.54 5.08 7.62]

# comparison using pure python without the NumPy library
# dimensions_inch = [1, 2, 3]
# dimensions_cm = [x * 2.54 for x in dimensions_inch]
# print(dimensions_cm)
