#Juego adivina mi número

import random

num_secreto = random.randint(1, 20)
intentos = 0
adivino = 0

while intentos < 5:
    numero = int(input("Ingrese un numero: "))
    intentos = intentos + 1
    if numero == num_secreto:
        print("Adivinaste! Mi numero era " + str(num_secreto))
        adivino = 1
        break
    elif numero < num_secreto:
        print("Mi numero es mayor\n")
    elif numero > num_secreto:
        print("Mi numero es menor\n")

if adivino == 0:
    print("No adivinaste! Mi numero era " + str(num_secreto))
      