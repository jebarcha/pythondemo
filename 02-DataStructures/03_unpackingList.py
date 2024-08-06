numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# list unpacking
# the number of variables should be equal to the number of items
first, second, third = numbers

# ------------------------------------
numbersMore = [1, 2, 3, 4, 5, 6, 7, 7, 8]
first, second, *other = numbersMore

print(first)
print(other)  # [3, 4, 5, 6, 7, 7, 7]

# what if we only care about first and last item?
first, *other, last = numbersMore
print(first)  # 1
print(other)  # [2, 3, 4, 5, 6, 7, 8]
print(last)  # 8
