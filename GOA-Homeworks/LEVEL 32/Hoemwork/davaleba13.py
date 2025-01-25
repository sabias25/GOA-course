# Create a function that inserts an item at the beginning of a list.

def insert_at_beginning(my_list, item):
    my_list.insert(0, item)
    print(my_list)

insert_at_beginning([1, 2, 3], 0)