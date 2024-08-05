course = "Python Programming"
print(len(course))  # returns 18
print(course[0])  # returns P
# retuns the first character from the end of the string, returns g
print(course[-1])
print(course[-2])  # retuns the second character from the end and so on. n

# returns all characters from start index (0) all the way to the end indes (3) but id doesn't include the character of the end index.
print(course[0:3])  # returns Pyt
print(course[:3])  # returns Pyt, same expression as previous 0:3
print(course[0:])  # returns the entire string
print(course[:])  # same result as previous [0:]

print(id(course))
print(id(course[0]))  # is different from id(course)


# --------------
# Formatted Strings:
first = "John"
last = "Lennon"
# full = first + " " + last
full = f"{first} {last}"
print(full)
full = f"{len(first)} {last} {2+2}"
print(full)
