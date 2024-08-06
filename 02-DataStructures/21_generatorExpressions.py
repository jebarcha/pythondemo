from sys import getsizeof

# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

# Generator Expression
# more efficient to use generator object, takes less memory
# generate a new value on each iteration
# values = (x * 2 for x in range(10))
# print(values)  # <generator object <genexpr> at 0x0000023322B7C520>
# for x in values:
#     print(x)

# better use a generator object:
valuesGen = (x * 2 for x in range(100000))
print("gen:", getsizeof(valuesGen))  # 200

valuesList = [x * 2 for x in range(100000)]
print("list:", getsizeof(valuesList))  # 800984
