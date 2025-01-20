# Write a function that returns the index of a character provided by the user in a string.


def find_character(input_string, char):
    index = input_string.find(char)
    return index

input_string = "saba tavadze"
char = input("Enter a character to find: ")
print(find_character(input_string, char))  