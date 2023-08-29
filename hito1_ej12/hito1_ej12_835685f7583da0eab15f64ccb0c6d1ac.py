#Juego adivina mi número
import random
nummin =  1
nummax = 20
adivnin = 0

numero_aleatorio = random.randint(nummin,nummax)
print("Adivina mi numero, esta entre",str(nummin),"y",str(nummax))

while adivnin < 5:
    print("Cual crees que es el numero?: ")
    intentos = input()
    intentos = int(intentos)

    adivnin = adivnin + 1
    if intentos < numero_aleatorio:
        print("Mi numero es mayor")
    if intentos > numero_aleatorio:
        print("Mi numero es menor")
    if intentos == numero_aleatorio:
        break
if intentos == numero_aleatorio:
    print("Adivinaste,mi numero era",numero_aleatorio)
if intentos != numero_aleatorio:
    numero_aleatorio = str(numero_aleatorio)
    print("No adivinaste,mi numero era",numero_aleatorio)