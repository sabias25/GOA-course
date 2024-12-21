my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input("შეიყვანეთ num1: "))
num2 = int(input("შეიყვანეთ num2: "))

if num1 > num2:
    new_list = my_list[num2:num1]  
    print("ახალი სია:", new_list)
elif num2 > num1:
    new_list = my_list[num1:num2]
    print("ახალი სია:", new_list)
else:
    print("ცარიელი სია: []")
