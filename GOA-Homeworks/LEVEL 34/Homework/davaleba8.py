# Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.

def get_positive_numbers(numbers):
    positive_numbers = []
    for i in numbers:
        if i > 0:
            positive_numbers.append(i)
    return positive_numbers

numbers = [-1, 2, -4, 5, 6, -7]
print(get_positive_numbers(numbers))  