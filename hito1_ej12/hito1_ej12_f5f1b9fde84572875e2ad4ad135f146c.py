#Juego adivina mi número
import random

num = random.randint(1, 20)
intentos = 0

while intentos < 5:
    num_i = int(input("Ingrese un numero: "))

    if num_i == num:
        print("Adivinaste, mi número era", num)
        break
    elif num_i > num:
        print("El número ingresado es mayor que el número secreto")
    else:
        print("El número ingresado es menor que el número secreto")

    intentos += 1

if intentos >= 5:
    print("No adivinaste, mi número era", num)      