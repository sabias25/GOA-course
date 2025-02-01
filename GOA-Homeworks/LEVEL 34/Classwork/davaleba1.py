# list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]

# list1.pop(3)
# print(list1)


# საკლასო დავალება:
# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.
# # თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები


def remove_elements(main_list, indexes_list):
    for index in indexes_list[::-1]:
        main_list.pop(index)

main_list = ["apple", "tomato", "cucumber", "strawbery", "potato"]

indexes_list = [2, 3]

remove_elements(main_list, indexes_list)

print(main_list)