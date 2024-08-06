letters = ["a", "b", "c"]
print(letters.count("d"))  # 0
print(letters.index("b"))  # 1
# print(letters.index("d"))  # error
if "d" in letters:
    print(letters.index("d"))
