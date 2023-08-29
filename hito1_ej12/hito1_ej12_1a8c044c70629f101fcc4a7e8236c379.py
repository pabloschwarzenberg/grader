#Inicio

import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a 'Adivina mi número'!")
    print("Tienes 5 intentos para adivinar un número del 1 al 20.")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste, mi número era", numero_secreto, "!")
            return

        if intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto)

adivina_mi_numero()
#Fin