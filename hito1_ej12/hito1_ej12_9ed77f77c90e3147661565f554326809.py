#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)

intentos = 5

print("Bienvenido al juego Adivina mi número. Tienes 5 intentos para adivinar el número secreto.")

while intentos > 0:
    numero = int(input("Ingresa un número entre 1 y 20: "))

    intentos -= 1

    if numero < numero_secreto:
        print("Mi número es mayor.")
    if numero > numero_secreto:
        print("Mi número es menor.")
    if numero == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break

    if intentos == 0:
        print("No adivinaste. Mi número era", numero_secreto)
        break

    print("Intentos restantes:", intentos)

print("Fin del juego.")
