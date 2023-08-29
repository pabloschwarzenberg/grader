#Juego adivina mi número
import random 

guessesTaken = 0
minNumber = 1
maxNumber = 20

print("hola! cual es tu nombre?: ")
username = input()

number = random.randint(minNumber, maxNumber)
print("bien," + username + ", estoy pensando en un numero entre" + str(minNumber) + "and" + str(maxNumber))

while guessesTaken < 5:
    print("elige un numero: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("mi numero es mayor.")
    if guess > number:
        print("mi numero es menor.")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print(" adivinaste, mi numero era " ,number)
if guess != number:
    number = str(number)
    print("No adivinaste, mi numero era" ,number)