import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego 'Adivina mi número'!")
    print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.\n")

    while intentos > 0:
        numero_adivinar = int(input("Ingresa tu número: "))

        if numero_adivinar == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        elif numero_adivinar < numero_secreto:
            print("Mi número es mayor.\n")
        else:
            print("Mi número es menor.\n")

        intentos -= 1
        print("Te quedan", intentos, "intentos.\n")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()

      