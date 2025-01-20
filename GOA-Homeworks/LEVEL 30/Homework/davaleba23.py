# Verify if all the characters in a user-provided string are uppercase.


def check_uppercase(input_string):
    if input_string.isupper():
        print("All characters are uppercase.")
    else:
        print("Not all characters are uppercase.")

input_string = input("Enter a string: ")
check_uppercase(input_string)