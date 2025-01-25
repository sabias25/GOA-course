# Create a function that appends all elements of one list to another list.

def append_all_to_list(list1, list2):
    list1.extend(list2)
    print(list1)

append_all_to_list([1, 2, 3], [4, 5, 6])