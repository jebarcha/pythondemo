# local variables -------
# def greet():
#     if True:
#         message = "a"
#     print(message)


# greet()

# global variables ------------
message = "a"


def greet():
    global message
    message = "b"  # this becomes a local variable in the greet() function
    # print(message) #here result is "b"


greet()
print(message)  # result is "a", unless we use the keyword global <varname>
