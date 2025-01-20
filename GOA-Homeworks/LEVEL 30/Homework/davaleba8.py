# Given a list of lowercase strings, capitalize the first letter of each string.



num1 = ['hello', 'world', 'python']
i = 0
while i < len(num1):
    num1[i] = num1[i].capitalize()
    i += 1
print(num1)