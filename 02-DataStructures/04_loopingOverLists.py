# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items  # we can unpack the tuple
# on each iteration will give us a "tuple", readonly
# if we need the index, we can use en enumerate function:
for index, letter in enumerate(letters):  # unpack using index, letter
    # print(letter)
    # print(letter[0], letter[1])
    print(index, letter)
