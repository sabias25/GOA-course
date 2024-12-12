
number = float(input("Enter a number: ")) 
if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "zero"

print(f"The number is {result}.")