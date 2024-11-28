# 9) Create a program that keeps asking for a username and password until both are correct.

correct_username = "saba"
correct_password = "12345678"

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password. Please try again.")
