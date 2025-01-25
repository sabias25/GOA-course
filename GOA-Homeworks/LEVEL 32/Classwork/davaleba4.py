# საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_append. ამ ფუნქციამ სიის ბოლოში უნდა ჩაამატოს ახალი ელემენტი.
# არ გამოიყენოთ append, გამოიყენეთ insert.
# ფუნქციას ექნება 2 პარამეტრი - main_list, item_to_insert.


def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

my_list = [1, 2, 3]
print("საწყისი სია:", my_list)

manual_append(my_list, 4)
print("განახლებული სია:", my_list)