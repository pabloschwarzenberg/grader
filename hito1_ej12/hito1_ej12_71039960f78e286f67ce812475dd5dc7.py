#Juego adivina mi número
import random

numRandom = random.randint(1,20)

print(numRandom)

intentos = 0

while intentos <=5:
    numero = int(input('Adivina el numero: '))
    if numero == numRandom:
        print("Adivinaste,mi numero era ",numRandom)
        break
    elif numRandom > numero:
        print("Mi numero es mayor")
    elif numRandom < numero:
        print("Mi numero es menor")
    
    intentos = intentos + 1
    if intentos == 5:
        print('No adivinaste, mi numero era ',numRandom)
        break      