# Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.

def csv_to_list(csv_string):
    items = csv_string.split(",")
    print(items)

csv_to_list("apple,banana,cherry")