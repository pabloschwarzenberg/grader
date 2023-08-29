#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("He generado un número secreto entre 1 y 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!\n")

    for i in range(intentos):
        print("Intentos restantes:", intentos - i)
        guess = int(input("Ingresa tu número: "))

        if guess == numero_secreto:
            print("¡Adivinaste! ¡Mi número era", numero_secreto, "!")
            return

        if guess < numero_secreto:
            print("Mi número es mayor.\n")
        else:
            print("Mi número es menor.\n")

    print("¡No adivinaste! Mi número era", numero_secreto, ".")

# Ejecutar el juego
adivina_mi_numero()