# Create a function that converts a list of lowercase strings to uppercase.



def convert_list_to_uppercase(strings):
    result = []
    for string in strings:
        result.append(string.upper())
    return result

lowercase_list = ['saba', 'giorgi', 'andria']
uppercase_list = convert_list_to_uppercase(lowercase_list)
print("Uppercase List:", uppercase_list)