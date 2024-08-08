try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
    # print("You didn't enter a valid age.")
    # print("Age cannot be 0.")
else:
    print("No exceptions were thrown")

print("Execution continues")
