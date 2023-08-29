#Juego adivina mi número
import random
guessesTaken= 0
minNumber= 1
maxNumber= 20

print("Hola, cual es tu nombre?: ")
username= input()

number= random.randint(minNumber, maxNumber)
print("Bueno, "+username+" estoy pensando en un numero entre "+str(minNumber)+" y "+str(maxNumber))

while guessesTaken<5:
    print("adivina el numero: ")
    guess= input()
    guess= int(guess)

    guessesTaken= guessesTaken+1

    if guess<number:
        print("tu numero es demasiado bajo.")
    if guess>number:
        print("tu numero es demasiado alto.")
    if guess==number:
        break
    
if guess==number:
print("Adivinaste, mi numero era: "+number+)

