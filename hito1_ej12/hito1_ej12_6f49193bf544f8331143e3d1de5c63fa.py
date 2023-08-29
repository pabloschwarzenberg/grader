#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("He generado un número entre 1 y 20. ¡Adivina cuál es!")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if intento < numero_secreto:
            print("Mi número es mayor.")

        if intento > numero_secreto:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
