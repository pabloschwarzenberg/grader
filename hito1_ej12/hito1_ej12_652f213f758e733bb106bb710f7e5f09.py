import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número.")
    print("Tienes que adivinar un número entre 1 y 20.")
    print("¡Buena suerte!\n")

    while intentos > 0:
        numero = int(input("Ingresa tu intento: "))

        if numero == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        elif numero < numero_secreto:
            print("Mi número es mayor\n")
        else:
            print("Mi número es menor\n")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)


# Ejecutar el juego
adivina_mi_numero()
