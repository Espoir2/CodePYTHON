from random import *

# Data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['+', '-', '*', '/', '.', 'µ', '£', 'ù', '%', '£', '$', '¤', '@', '#', '&']

# Users input
a = int(input("How many letters would you like in your password?\n"))
b = int(input("How many numbers would you like?\n"))
c = int(input("How many symbols would you like?\n"))

# PassWord elements
list_letters = []
list_numbers = []
list_symbols = []

for _ in range(0, a):  # or use choices(letters, k = a)
    list_letters.append(choice(letters))
print(list_letters)

for _ in range(0, b):
    list_numbers.append(choice(numbers))
print(list_numbers)

for _ in range(0, c):
    list_symbols.append(choice(symbols))
print(list_symbols)

total = list_letters + list_numbers + list_symbols
# print(total)

print("Here is your low level password : ")
for i in total: # or use print(''.join(total))
    print(i, end="")
print()

print("Here is your high level password : ")
pass_word = []
pass_word += total[0::3]
pass_word += total[1::3]
pass_word += total[2::3]

# for i in pass_word:
#     print(i, end="")

print(''.join(pass_word))

shuffle(pass_word)
print(f"Here is your very high level password : {''.join(pass_word)}")




