numbers = [1, 2]
# print(numbers[3])

# age = int(input("Age: "))

# how to handle exceptions

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)  # invalid literal for int() with base 10: 'A'
    print(type(ex))  # <class 'ValueError'>
else:
    print("No exceptions were thrown")
print("Execution continues")
