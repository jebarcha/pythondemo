try:
    # with open("README.md") as file, open("another.txt") as target:  # will delete external resources automatically
    with open("README.md") as file:
        print("File openend.")
        # file.__exit__  if contains __exit or __enter, we can use the "with" statement to release external resources

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

print("Execution continues")
