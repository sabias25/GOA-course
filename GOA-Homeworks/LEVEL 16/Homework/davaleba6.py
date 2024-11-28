# 8) Prompt the user to enter a password. Keep asking until they enter the correct password.

correct_password = "12345678"

while True:
    entered_password = input("Please enter your password: ")

    if entered_password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Please try again.")


