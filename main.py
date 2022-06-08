import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9',]
symbols = ['!','#','$','%','&','(',')','*','+']


print("welcome to Password Generator")

letter = int(input("How many letters would you like in your password?"))
symbol = int(input("How many symbols would you like in your password?"))
number = int(input("How many numbers would you like in your password?"))

sum = letter + symbol + number
password = ""

for i in range(sum):
    choice = random.randint(0,2)
    if(choice == 0 and letters != 0):
        randomLetter = letters[random.randint(0,len(letters) - 1)]
        password = password + randomLetter
        letter = letter - 1
    elif (choice == 1 and symbol != 0):
        randomSymbol = symbols[random.randint(0, len(symbols) - 1)]
        password = password + randomSymbol
        symbol = symbol - 1
    elif (choice == 2 and number != 0):
        randomNum = numbers[random.randint(0, len(numbers) - 1)]
        password = password + randomNum
        number = number - 1
    else:
        i = i - 1

print(password)