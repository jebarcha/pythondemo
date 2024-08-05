# names = ["John", "Paul"]
# names = ["AJohn", "Paul"]
# found = False
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")

# We have for else blocks in python
names = ["AJohn", "Paul"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")
