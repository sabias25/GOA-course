
number = int(input("Enter a number: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if is_prime(number):
    print(f"The number {number} is a prime number.")
else:
    print(f"The number {number} is not a prime number.")
