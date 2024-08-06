browsing_session = []

# use append to add an item on top of the stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# use pop to remove an item from top of the stack (and return it)
last = browsing_session.pop()
print(last)
print(browsing_session)

# if stack is empty, check if falsy, remember 0, "" or [] are falsies
if not browsing_session:
    print("disable buttons")

# use index -1, to get the item on top of the stack (the last item)
print("redirect", browsing_session[-1])
