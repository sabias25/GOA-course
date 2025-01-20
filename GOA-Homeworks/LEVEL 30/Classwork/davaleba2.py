# შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.
# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.
# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1


def manual_find(main_string, str_to_find):
    return main_string.find(str_to_find)

main_string = "saba"
str_to_find = "tavadze"
print(manual_find(main_string, str_to_find))  