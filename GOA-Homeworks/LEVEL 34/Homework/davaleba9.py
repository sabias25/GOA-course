# Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.

def sum_divisible_by_three(start, end):
    total_sum = 0
    for i in range(start, end + 1):
        if i % 3 == 0:
            total_sum += i
    return total_sum

result = sum_divisible_by_three(1, 100)
print(result)  