"""The objective is to take the inputs from the user to these questions and then generate a random password. 
Use your knowledge about Python lists and loops to complete the challenge."""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Have a loop to generate random characters by indexing the lists above
password = ""

for i in range(nr_letters):
    password += letters[random.randint(0, len(letters)-1)]

for i in range(nr_symbols):
    password += symbols[random.randint(0, len(symbols)-1)]

for i in range(nr_numbers):
    password += numbers[random.randint(0, len(numbers)-1)]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# If there are still characters of a certain type to be added, randomly select a function to run
password = ""

while nr_numbers or nr_letters or nr_symbols:
    char_type = random.randint(0,2)

    if nr_numbers > 0 and char_type == 0:
        password += letters[random.randint(0, len(letters)-1)]
        nr_numbers -= 1
    elif nr_letters > 0 and char_type == 1:
        password += symbols[random.randint(0, len(symbols)-1)]
        nr_letters -= 1
    elif nr_symbols > 0 and char_type == 2:
        password += numbers[random.randint(0, len(numbers)-1)]
        nr_symbols -= 1

print(password)