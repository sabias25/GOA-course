# # საკლასო დავალება:
# #  შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.

# # სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.

# # საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.

# # დაგჭირდებათ while loop, counter variable
# correct_password = "my_secure_password"

# attempts = 0

# while True:
#     user_input = input("შეიყვანეთ პაროლი: ")
    
#     attempts += 1
    
#     if user_input == correct_password:
#         print("Access granted")
#         break

# print(f"თქვენ {attempts} მცდელობა დაგჭირდათ.")


# მეორე დავალება

my_num = 7 

attempts = 0

while True:
    user_guess = int(input("გამოიცანი რიცხვი 1-დან 10-მდე: "))
    
    attempts += 1
    
    if user_guess == my_num:
        print("You guessed!")
        break

print(f"მოგიწიათ {attempts} მცდელობა რიცხვის გამოსაცნობად.")
