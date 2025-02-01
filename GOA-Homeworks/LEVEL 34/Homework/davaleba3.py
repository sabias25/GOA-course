# Return Statement: Create a function that takes a number as input, multiplies it by 10, and returns the result.


def multiply_by_ten(number):
    return number * 10

number = input("Enter your number: ")
result = multiply_by_ten(number)

print(f"{number} multiplied by 10 is: {result}")