#Juego adivina mi número
import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

number = random.randint(minNumber, maxNumber)


while guessesTaken < 5:
    print("Estoy pensando en un numero entre el 1 y el 20, cual piensas que es?: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("mi numero es mayor")
    elif guess > number:
        print("mi numero es menor")
    elif guess == number:
        break

if guess == number:
    number = str(number)
    print("Adivinaste, mi número era", number)
elif guess != number:
    print("No adivinaste, mi número era", number)
