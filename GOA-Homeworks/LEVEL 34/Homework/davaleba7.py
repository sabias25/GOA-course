# Find the Maximum
# Create a function that takes a list of numbers and uses a loop to find and return the maximum number.


def find_max(numbers):
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number

numbers = [1, 4, 2, 3, 10, 3, 5]
print(find_max(numbers))  