# Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.


def is_uppercase(input_string):
    return input_string.isupper()

input_string = input("Enter a string: ")
result = is_uppercase(input_string)
print(result)  