# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_index, რომელსაც ექნება 2 პარამეტრი - მთავარი სთრინგი და საძიებელი სთრინგი.
# თქვენი დავალებაა რომ დააბრუნოთ მთავარ სთრინგში საძიებელი სთრინგი მერამდენე ინდექსზეა

def manual_index(main_string, search_string):
    search_len = len(search_string)
    
    for i in range(len(main_string) - search_len + 1):
        if main_string[i:i+search_len] == search_string:
            return i  
    
    return -1

main_string = "Hello, world!"
search_string = "world"
print(manual_index(main_string, search_string)) 
