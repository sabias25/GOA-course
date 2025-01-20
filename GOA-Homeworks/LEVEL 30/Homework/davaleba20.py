#  Check if all characters in a given string are lowercase and print the result.


def check_lowercase(input_string):
    if input_string.islower():
        print("All characters are lowercase.")
    else:
        print("Not all characters are lowercase.")

input_string = "saba"
check_lowercase(input_string) 