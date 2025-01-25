# Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.

def welcome_message(name, age):
    print(f" welcome to new school, my name is {name}, and i am {age} years old  ")

name = input("enter your name: ")
age = input("Enter your age: ")

welcome_message(name, age)