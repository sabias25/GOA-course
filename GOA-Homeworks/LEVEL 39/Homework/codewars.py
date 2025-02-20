# 1 

def filter_list(lst):
    return [i for i in lst if isinstance(i, int)]

print(filter_list([1, 2, 'a', 'b', 3]))  


# 2

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

quote = "how can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))  

# 3

def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(int(digit) for digit in str(n)))

print(digital_root(942))  

# 4

def filter_list(lst):
    return [i for i in lst if isinstance(i, int)]

print(filter_list([1, 2, 'a', 'b', 3])) 
print(filter_list([5, 'hello', 10, 'world', 15]))  

# 5

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

quote = "how can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))  
