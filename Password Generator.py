import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
'נ', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', '0', '', 'w', 'x', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwordList = []
for i in range(1,nr_letters+1):
    randLetter = random.choice(letters)
    passwordList += randLetter
for n in range(1,nr_symbols+1):
    randSymb = random.choice(symbols)
    passwordList += randSymb
for a in range(1,nr_numbers+1):
    randNum = random.choice(numbers)
    passwordList += randNum

random.shuffle(passwordList)
print("".join(passwordList))


