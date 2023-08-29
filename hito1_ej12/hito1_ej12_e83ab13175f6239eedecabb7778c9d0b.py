#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego Adivina mi número")

for i in range(intentos):
    numero_ingresado = int(input("Intento {}/{} - Ingresa un número del 1 al 20: ".format(i + 1, intentos)))

    if numero_ingresado == numero_secreto:
        print("Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

    if i == intentos - 1:
        print("No adivinaste. Mi número era", numero_secreto)

print("Gracias por jugar")
