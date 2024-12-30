# Get the first element from a list.

my_list = [10, 20, 30, 40]
first_element = my_list[0]
print(first_element)  

# Get the last element from a list using negative indexing.

my_list = [10, 20, 30, 40]
last_element = my_list[-1]
print(last_element)  

# Slice the first three elements of a list.

my_list = [10, 20, 30, 40, 50]
first_three_elements = my_list[:3]
print(first_three_elements)

# Extract the last five elements from a string.

my_string = "Hello, World!"
last_five = my_string[-5:]
print(last_five)  

# Reverse a string using slicing.

my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)

# Get every third element from a list - ყოველი მესამე ელემენტი სიიდან

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
every_third = my_list[::3]
print(every_third)  

# Split a list into two halves using slicing. - ორ ნაწილად დაყავით სია (სიის სიგრძე აიღეთ ლუწი)


my_list = [1, 2, 3, 4, 5, 6]
midpoint = len(my_list) // 2  
first_half = my_list[:midpoint]
second_half = my_list[midpoint:]

print(first_half)   
print(second_half) 