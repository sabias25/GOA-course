#  Write a function that replaces all spaces in a string with underscores.


def replace_spaces_with_underscores(input_string):
    return input_string.replace(" ", "_")

input_string = "my car is going fast"
new_string = replace_spaces_with_underscores(input_string)
print(new_string) 