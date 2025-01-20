# Write a function that takes a list of strings and returns their lengths.

def find_lengths_of_strings(strings):
    lengths = []
    for string in strings:
        lengths.append(len(string))
    return lengths

strings = ["saba", "andria", "giorgi"]
print(find_lengths_of_strings(strings))
