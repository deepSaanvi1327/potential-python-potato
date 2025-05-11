import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to Password Generator")
print("Password contains Letters, Numbers and Symbols")
n_letters = int(input("How many letters? "))
n_numbers = int(input("How many numbers? "))
n_symbols = int(input("How many symbols? "))

pswd_characters = n_letters + n_numbers + n_symbols

password = []

for char in range(1,n_letters + 1):
    password.append(random.choice(letters))


for char in range(1,n_numbers + 1):
    password.append(random.choice(numbers))


for char in range(1,n_symbols + 1):
   password.append(random.choice(symbol))


random.shuffle(password)
res = ''.join(password)
print(res)
