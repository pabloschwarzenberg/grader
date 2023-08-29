#Juego adivina mi número
 import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos > 0:
        numero = int(input("Ingresa un número del 1 al 20: "))

        if numero < numero_secreto:
            print("Mi número es mayor.")
        elif numero > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()     