# Boss level: Use a while loop to calculate the factorial of a given number.

num = int(input("Enter a number to calculate its factorial: "))

factorial = 1

temp = num

while temp > 0:
    factorial *= temp  
    temp -= 1  


print(f"The factorial of {num} is {factorial}")
