# დავალება 1
def multiply(a, b):
    return a * b

# დავალება 2

def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else: return "Odd"

# დავალება 3

def number_to_string(num):
    return str(num)

# დავალება 4

def solution(string):
    return string[::-1]

# დავალება 5

def make_negative( number ):
    return number if number < 0 else -number

# დავალება 6

def opposite(number):
    return -number 

# დავალება 7

def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"
    
# დავალება 8

def positive_sum(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res

# დავალება 9

def repeat_str(repeat, string):
    res = ""
    for i in range(repeat):
        res = res + string
    return res

# def repeat_str(repeat, string):
    # return string * repeat

# დავალება 10

def remove_char(s):
    return s[1:-1]

# დავალება 11

def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i**2
    return result