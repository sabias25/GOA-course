# Write a function that takes a list, an index, and an item, and inserts the item at the specified index.

def insert_at_index(my_list, index, item):
    my_list.insert(index, item)
    print(my_list)


insert_at_index([1, 2, 3], 1, 4)