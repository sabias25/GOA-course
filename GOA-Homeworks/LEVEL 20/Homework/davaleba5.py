
start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

if start > end:
    start, end = end, start

sum_of_numbers = 0
for number in range(start, end + 1):
    sum_of_numbers += number

print(f"The sum of numbers between {start} and {end} is: {sum_of_numbers}")