# collection of key - value pairs
# name -> contact

# point = {"x": 1, "y": 2}
# print(point) # {'x': 1, 'y': 2}

point = dict(x=1, y=2)
print(point)  # {'x': 1, 'y': 2}

# access values by the name of the key
print(point["x"])  # 1

# change the value of x
point["x"] = 10
print(point)  # {'x': 10, 'y': 2}

point["z"] = 20
print(point)  # {'x': 10, 'y': 2, 'z': 20}

# accessing with unexisting key, will get error
# print(point["a"])

# we can check for the existance of a key
if "a" in point:
    print(point["a"])

print(point.get("a"))  # returns: None
print(point.get("a", 0))  # returns 0 if key "a" doest not exist

# delete, use del
del point["x"]
print(point)  # {'y': 2, 'z': 20}

# -----------------------------
# Loop over dictionaries
# for key in point:
#     print(key, point[key])  # the key holds the key of an item

for x in point.items():
    print(x)  # we get a tu tuple on each iteration with the key and value

# as it is a tuple of each iteration, we can unpack it:
for key, value in point.items():
    print(key, value)
