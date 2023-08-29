#Juego adivina mi número
import random

intentos = 0

numSecreto = random.randint(1, 20)

while intentos != 5:

    numElegido = int(input("Ingrese un numero entre 0 y 20: "))
    if numElegido == numSecreto:
        print("Adivinaste, El número era {}".format(numSecreto))
        break
    elif numElegido > numSecreto:
        print("El número es menor")
        intentos += 1
    else:
         print("El número es mayor")
         intentos += 1
if intentos == 0:
    print("Rayos No adivinaste, El número era {}".format(numSecreto))