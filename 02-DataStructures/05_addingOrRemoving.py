letters = ["a", "b", "c"]

# Add, depend where you want to add it
letters.append("d")  # adding at the end
letters.insert(0, "-")  # adding at the beggining
# print(letters)

# Remove
letters.pop()  # remove at the end
letters.pop(0)  # pass an index to remove an item from the given index
letters.remove("b")  # remove "b", it removes the first occurance
del letters[0:3]  # with del can remove a range of items
letters.clear()  # remove all
print(letters)
