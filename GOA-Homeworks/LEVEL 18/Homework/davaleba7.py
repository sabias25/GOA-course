correct_password = "Goa best"

incorrect_count = 0

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Access granted.")
        break  
    else:
        incorrect_count += 1
        print(f"Incorrect password. Attempt {incorrect_count}.")

print(f"You entered the incorrect password {incorrect_count} times.")
