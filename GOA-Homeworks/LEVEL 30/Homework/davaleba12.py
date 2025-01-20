# Write a function to find and return the index of a specified character in a given string.

def find_character_index(text, character):
    return text.find(character)

num = "saba"
character = "a"
print(find_character_index(num, character))