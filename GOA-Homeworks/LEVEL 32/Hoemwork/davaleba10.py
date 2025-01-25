# Create a function that takes a list and a list of items, and appends each item to the original list.

def add_multiple_to_list(my_list, items):
    for item in items:
        my_list.append(item)
    print(my_list)

add_multiple_to_list([1, 2, 3], [4, 5, 6])