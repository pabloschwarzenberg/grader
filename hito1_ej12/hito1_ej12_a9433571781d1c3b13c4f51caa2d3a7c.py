import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos > 0:
        print("Intentos restantes:", intentos)
        numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        elif numero_ingresado > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste, mi número era", numero_secreto, "!")
            return

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto, ".")

adivina_mi_numero()