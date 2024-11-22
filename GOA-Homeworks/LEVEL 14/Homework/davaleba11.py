num1 = int(input("enter your first number (num1): "))
num2 = int(input("enter tour second number (num2): "))
num3 = int(input("enter your third number (num3): "))

for i in range(num1, num2, num3):
    print(i ** 2)