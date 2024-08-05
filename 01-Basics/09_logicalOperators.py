# Python Logical Operators
# and
# or
# not

# name = " "  # ""  # "Paul"
# # "" => False -> True
# if not name.strip():
#     print("Name is empty")
# else:
#     print("Name is not empty")


# age = 22
# if age >= 19 and age < 65:
#     print("Elegible")

# write the expression in Math?
# 18 <= age < 66  #this is known as: "chaining comparison operators"
# That is why python is highly popular because we can for example rewrite that expression
# in a simplear, more meaninful way. it is clean without any clutter and easy to understand.
# and it comes with all these best standars and practices for writing clean code.
age = 22
if 18 <= age < 64:
    print("Elegible")

# ------------------------
# Ternary Operator - write in a more compact way
# ------------------------
# in other languages like C#, javascript, java, etc: message = age >= 18 ? "Elegible": "Not elegible"
# the python way:
message = "Elegible" if age >= 18 else "Not elegible"
print(message)
