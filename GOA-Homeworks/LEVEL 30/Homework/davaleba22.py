# Prompt the user to input a string and verify if it contains only lowercase letters.


input_string = input("Enter a string: ")

if input_string.islower():
    print("The string is all lowercase.")
else:
    print("The string contains uppercase letters or other characters.")
