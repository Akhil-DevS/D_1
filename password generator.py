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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letter_len=len(letters)
num_len=len(numbers)
sym_len=len(symbols)
x=random.randint(0,letter_len-1)
lettering=[letters[x]]
x=random.randint(1,num_len-1)
numbering=[numbers[x]]
x=random.randint(1,sym_len-1)
symboling=[symbols[x]]
for n in range(1,nr_letters):
  x=random.randint(0,letter_len-1)
  lettering.append(letters[x])
for n in range(1,nr_numbers):
    x=random.randint(1,num_len-1)
    numbering.append(numbers[x])
for n in range(1,nr_symbols):
    x=random.randint(1,sym_len-1)
    symboling.append(symbols[x])
total=nr_symbols+nr_numbers+nr_letters
print(f'{lettering}\n{numbering}\n{symboling}')
# pass_word=[lettering,numbering,symboling]
# passowrd=''
# for n in lettering:
#     passowrd+=str(n)
# for n in numbering:
#     passowrd+=str(n)
# for n in symboling:
#     passowrd+=str(n)
real_password=''
for n in range(0,total-1):
    if n<nr_letters:
        real_password+=str(random.choice(letters))
    if n<nr_numbers:
        real_password+=str(random.choice(numbers))
    if n<nr_symbols:
        real_password+=str(random.choice(symbols))
print(real_password)

password = []
for x in range(0,nr_letters):
  password.append(random.choice(letters))
for y in range(0,nr_numbers):
  password.append(random.choice(numbers))
for z in range(0,nr_symbols):
  password.append(random.choice(symbols))
random.shuffle(password)
final_pass = ""
for a in range (0,len(password)):
  final_pass = final_pass + str(password[a])
print(final_pass)