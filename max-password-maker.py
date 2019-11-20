#!/usr/bin/python3

# Coded by: Max Silveri
# Date: 11/20/19
# Age: 11

x = input("\nName a Place you would like to go to: ")
v = input("\nDescribe that place with an adjective: ")
w = input("\nWhat is your favorite number: ")

password = w + v + x

print("\n\n")
print("your generated password is: " + password)

if len(password)<10:
    print("THIS IS A WEAK PASSWORD, IT IS TOO SHORT")
else:
    print("THIS IS A STRONG PASSWORD GREAT JOB!")
