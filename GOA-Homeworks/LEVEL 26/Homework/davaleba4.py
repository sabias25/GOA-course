def find_max(num_list):
    max_value = num_list[0]

    for num in num_list:
        if num > max_value:
            max_value = num

    print("Max value")


find_max([1, 4, 2, 3, 10, 3, 5])