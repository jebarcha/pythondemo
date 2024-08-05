course = "  Python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())  # it the trime
print(course.rstrip())  # it the right trime

print(course.find("pro"))  # case sensitive

print(course.lower().find("pro"))  # case sensitive

print(course.replace("P", "-"))  # case sensitive

print("programming" in course)  # returns: true
print("programming" not in course)  # returns: false
