from pprint import pprint

sentence = "This is a common interview question"
# write a program to find the most repetead character in the text

# We need to know how many times a character is repeated
# Once we have that information, we can find the most repeated character.
# What data structure is more useful for storing this information? A Dictionary
# we can use the character as the key, and the repetiontion or counter as a value
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)

# sort the dictionary by the frequency of char
# but dictionaries cannot be sorted (same as sets)
# We need to pull out the items in the dictionary and put them in a list for sorting.
# Basically we need to take out each key-value pair, convert it to a tuple and then put it in a list.
# we will end up with a list of tuples that can be easily sorted.

# list of tuples. [(' ', 5), ('T', 1), ('a', 1) ...]
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])  # ('i', 5)
