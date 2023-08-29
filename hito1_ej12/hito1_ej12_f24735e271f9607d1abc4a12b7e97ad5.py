#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
max_intentos = 5
intentos = 0

print("¡Bienvenido al juego Adivina mi número!")

while intentos < max_intentos:
    numero = int(input("Ingresa un número entre 1 y 20: "))

    intentos += 1

    if numero == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        exit()

    if numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

print("No adivinaste. Mi número era", numero_secreto)