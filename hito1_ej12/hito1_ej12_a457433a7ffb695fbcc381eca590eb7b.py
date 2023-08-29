import random

guessesTaken = 0
minNumber = 1
maxNumber= 20


print('username '+ 'ingresa un numero entre ' ' ' +str(minNumber) + ' y ' + str(maxNumber))
number = random.randint(minNumber,maxNumber)
print('adivina el numero')
while guessesTaken <5:
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken +1
    if guess < number:
        print("mi numero es mayor")
    if guess > number:
        print("mi numero es menor")
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Adivinaste, mi número era "+ str(number))
if guess!=number:
    number = str(number)
    print("No adivinaste, mi número era "+str(number))