num1 = float(input("Enter the first number: "))

operator = input("Enter an operator (+, -, *, /): ")

num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
else:
    if operator == "-":
        result = num1 - num2
    else:
        if operator == "*":
            result = num1 * num2
        else:
            if operator == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error! Division by zero."
            else:
                result = "Invalid operator."

print(f"The result is: {result}")
