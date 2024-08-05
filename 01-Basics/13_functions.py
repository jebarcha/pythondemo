# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(increment(2, by=3))
# print(increment(2))

# --------------------------
# def multiply(a, b):
#     return a * b

# print(multiply(2, 3))

# def multiply(*list):  # python automatically packet it as a tuple
#     # print(list)  # we will get a tuple
#     total = 1
#     for number in list:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

# ----------------------
def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1, name="admin")
