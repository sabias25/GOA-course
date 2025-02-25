# 1 #

def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    
    total = 0
    for i in range(begin, end + 1, step):
        total += i
    
    return total

print(sequence_sum(2, 6, 2))  
print(sequence_sum(1, 5, 1))  
print(sequence_sum(1, 5, 3))
print(sequence_sum(2, 10, 3)) 


# 2 #

def logical_calc(values, op):
    if not values:
        return False  
    
    if op == "AND":
        result = values[0]
        for val in values[1:]:
            result = result and val  
        return result
    
    elif op == "OR":
        result = values[0]
        for val in values[1:]:
            result = result or val  
        return result
    
    elif op == "XOR":
        result = values[0]
        for val in values[1:]:
            result = result ^ val  
        return result
    
    else:
        raise ValueError("Invalid logical operator")  

print(logical_calc([True, True, False], "AND"))  
print(logical_calc([True, True, False], "OR"))  
print(logical_calc([True, True, False], "XOR"))  

# 3 #

def count_lowercase_letters(s):
    count = 0  
    for char in s:  
        if char.islower(): 
            count += 1  
    return count  

print(count_lowercase_letters("abc"))  
print(count_lowercase_letters("abcABC123")) 
print(count_lowercase_letters("abcABC123!@€£#$%^&*()_-+=}{[]|':;?/>.<,~"))  
print(count_lowercase_letters(""))  
print(count_lowercase_letters("ABC123!@€£#$%^&*()_-+=}{[]|':;?/>.<,~"))  
print(count_lowercase_letters("abcdefghijklmnopqrstuvwxyz"))  

# 4 #

def small_enough(arr, limit):
    for num in arr:  
        if num > limit: 
            return False
    return True  

print(small_enough([1, 2, 3, 4], 5))  
print(small_enough([1, 2, 3, 6], 5))  
print(small_enough([10, 20, 30], 25)) 
print(small_enough([1, 2, 3], 3))  

# 5 #

def mpg_to_kpl(mpg):
    kpl = mpg * 1.609344 / 4.54609188
    return round(kpl, 2)

print(mpg_to_kpl(10))  
print(mpg_to_kpl(25))  
print(mpg_to_kpl(50))  
print(mpg_to_kpl(100)) 