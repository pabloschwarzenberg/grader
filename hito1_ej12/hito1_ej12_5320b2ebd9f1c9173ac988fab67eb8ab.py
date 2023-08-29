#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

while intentos > 0:
    intentos -= 1
    numero = int(input("Adivina mi número: "))
    if numero == numero_secreto:
        print("Adivinaste, mi número era {}".format(numero_secreto))
        break
    elif numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if intentos == 0:
    print("No adivinaste, mi número era {}".format(numero_secreto))
