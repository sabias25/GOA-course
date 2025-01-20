# Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.


def is_lowercase(input_string):
    return input_string.islower()

input_string = "saba"
result = is_lowercase(input_string)
print(result) 